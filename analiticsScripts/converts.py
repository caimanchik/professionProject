import csv
from queue import Queue
from threading import Thread

import requests
import xml.etree.ElementTree as ET


def create_convert():
    results = Queue()
    threads = []
    window = [2003, 2022]

    for year in range(window[0], window[1] + 1):
        for month in range(1, 13):
            th = Thread(target=get_convert_year, args=(year, str(month) if month >= 10 else f"0{month}", results))
            threads.append(th)
            th.start()

    for th in threads:
        th.join()

    headers = set([header for data in results.queue for header in data.keys()])
    headers.remove('date')

    with open('csv_files/convert.csv', 'w', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['date'] + list(headers))

        for e in sorted(results.queue, key=lambda x: x['date']):
            line = [e['date']] + [e[header] if header in e.keys() else '' for header in headers]
            writer.writerow(line)


def get_convert_year(year: int, month: str, results: Queue):

    url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req=01/{month}/{year}'
    response = requests.get(url)

    valcurs = ET.fromstring(response.content)

    convert_dict = {'date': f"{year}-{month}"}

    for valute in list(valcurs):
        nominal = 0
        value = 0
        name = ''

        for item in list(valute):
            if item.tag == 'Nominal': nominal = float(item.text.replace(',', '.'))
            if item.tag == 'Value': value = float(item.text.replace(',', '.'))
            if item.tag == 'CharCode': name = item.text

        convert_dict[name] = value / nominal

    results.put(convert_dict)


if __name__ == '__main__':
    create_convert()