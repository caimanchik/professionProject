import re
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from functools import reduce
from typing import List, Dict


class Graph:

    __titles = [
        'Уровень зарплат по годам',
        'Количество вакансий по годам',
        'Уровень зарплат по городам',
        'Доля вакансий по городам',
    ]

    def __init__(self, vacancy: str):
        self.__vacancy = vacancy

    def draw(
            self,
            s_all: Dict[str, List[int]],
            s_filtered: Dict[str, List[int]],
            fract: List[List[float]],
            cities_s: List[List[int]]
    ):
        plt.rcParams['axes.facecolor'] = 'f0f1ff'
        plt.rcParams['savefig.facecolor'] = 'f0f1ff'

        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)

        Graph.__create_bar(
            ax1,
            s_all,
            s_filtered,
            0,
            ['Средняя з/п', f'З/п {self.__vacancy}'],
            Graph.__titles[0]
        )

        Graph.__create_bar(
            ax2,
            s_all,
            s_filtered,
            1,
            ['Количество вакансий', f'Количество вакансий {self.__vacancy}'],
            Graph.__titles[1]
        )

        Graph.__create_barh(ax3, cities_s[:10], Graph.__titles[2])
        Graph.__create_pie(ax4, fract[:10], Graph.__titles[3])

        fig.tight_layout()
        fig.set_size_inches(8, 6)
        fig.set_dpi(300)
        fig.savefig('graph.png', dpi=300)

        plt.show()


    @staticmethod
    def __create_bar(
            ax,
            data1: Dict[str, List[int]],
            data2: Dict[str, List[int]],
            index: int,
            legend: List[str],
            title: str
    ):
        width = 0.35
        labels_x = data1.keys()
        first = Graph.__get_data(data1, index)
        second = Graph.__get_data(data2, index)
        points = range(len(labels_x))

        ax.bar(list(map(lambda x: x - width / 2, points)), first, width, label=legend[0])
        ax.bar(list(map(lambda x: x + width / 2, points)), second, width, label=legend[1])
        ax.set_title(title)
        ax.legend(prop={'size': 8})
        ax.grid(axis='y')

        for label in ax.get_yticklabels():
            label.set_fontsize(8)

        ax.set_xticks(points, labels_x, fontsize=8, rotation=90)

    @staticmethod
    def __create_barh(ax, data: List[List[float]], title: str):
        cities = list(map(lambda x: Graph.__refactor_label(x[0]), data))
        y_pos = list(range(len(cities)))

        ax.barh(y_pos, list(map(lambda x: x[1], data)), align='center')

        ax.set_yticks(y_pos, labels=cities, fontsize=6)
        ax.invert_yaxis()
        ax.grid(axis='x')

        for label in ax.get_xticklabels():
            label.set_fontsize(8)

        ax.set_title(title)

    @staticmethod
    def __create_pie(ax, data: List[List[float]], title: str):
        cities = list(map(lambda x: x[0], data)) + ['Другие']
        others = 1 - reduce(lambda x, y: x + y[1], data, 0)

        ax.pie(list(map(lambda x: x[1], data)) + [others],
               labels=cities, textprops={'size': 6}, colors=mcolors.BASE_COLORS)

        ax.set_title(title)

    @staticmethod
    def __refactor_label(label: str) -> str:
        spaces = re.compile('\s+')
        line = re.compile('-+')

        label = re.sub(spaces, '\n', label)
        return re.sub(line, '-\n', label)


    @staticmethod
    def __get_data(data: Dict[str, List[int]], i: int) -> List[int]:
        return list(map(lambda x: x[i], data.values()))


if __name__ == '__main__':
    salaries = {'2003': 41304, '2004': 42967, '2005': 44938, '2006': 41317, '2007': 44449, '2008': 48411, '2009': 44811, '2010': 44657, '2011': 46448, '2012': 47969, '2013': 53541, '2014': 49076, '2015': 51734, '2016': 61305, '2017': 60363, '2018': 65581, '2019': 69938, '2020': 72833, '2021': 83061, '2022': 95473}
    salaries_vac = {'2003': 20086, '2004': 26592, '2005': 30155, '2006': 30825, '2007': 39915, '2008': 41326, '2009': 39359, '2010': 40685, '2011': 43249, '2012': 46498, '2013': 46761, '2014': 48973, '2015': 52025, '2016': 53114, '2017': 58626, '2018': 61267, '2019': 68327, '2020': 74302, '2021': 84711, '2022': 95434}
    count = {'2003': 1983, '2004': 7833, '2005': 16022, '2006': 33321, '2007': 53562, '2008': 75070, '2009': 52889, '2010': 93494, '2011': 142458, '2012': 173897, '2013': 234019, '2014': 259571, '2015': 284763, '2016': 332460, '2017': 391464, '2018': 517670, '2019': 535956, '2020': 489472, '2021': 287915, '2022': 91142}
    count_vac = {'2003': 8, '2004': 36, '2005': 101, '2006': 368, '2007': 590, '2008': 873, '2009': 719, '2010': 1206, '2011': 2300, '2012': 2389, '2013': 3135, '2014': 3397, '2015': 4306, '2016': 5550, '2017': 6386, '2018': 6913, '2019': 5701, '2020': 4173, '2021': 1743, '2022': 460}
    area_sal = [('Минск', 94092), ('Киев', 79895), ('Москва', 78957), ('Санкт-Петербург', 68747), ('Новосибирск', 64771), ('Екатеринбург', 59139), ('Краснодар', 51585), ('Казань', 51309), ('Нижний Новгород', 49914), ('Самара', 49548)]
    area_count = [('Москва', 0.334026018899322), ('Санкт-Петербург', 0.10140489688122169), ('Минск', 0.04061388562982566), ('Киев', 0.032169142232281484), ('Новосибирск', 0.023631882611882666), ('Нижний Новгород', 0.02144437701366958), ('Екатеринбург', 0.019727059964500273), ('Алматы', 0.01892116268106615), ('Воронеж', 0.018596006194905916), ('Казань', 0.01856606725806701), ('Ростов-на-Дону', 0.01388700407194081), ('Краснодар', 0.013454607295628106), ('Самара', 0.012670550712019083), ('Пермь', 0.010215312490107268)]

    s_all = {}
    s_filtered = {}

    for year in salaries.keys():
        s_all[year] = [salaries[year], count[year]]
        s_filtered[year] = [salaries_vac[year], count_vac[year]]

    image_generator = Graph('Web-программист')
    image_generator.draw(
        s_all,
        s_filtered,
        area_count,
        area_sal
    )