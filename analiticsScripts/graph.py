import re
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from functools import reduce
from typing import List, Dict, Tuple


class Graph:

    __titles = [
        'Уровень зарплат по годам',
        'Количество вакансий по годам',
        'Уровень зарплат по городам',
        'Доля вакансий по городам',
    ]

    def __init__(self, vacancy: str):
        self.__vacancy = vacancy

    def draw_skills(self, skills_arr: List[Tuple[str, int]], year: str):
        plt.rcParams['axes.facecolor'] = 'f0f1ff'
        plt.rcParams['savefig.facecolor'] = 'f0f1ff'
        fig, ax = plt.subplots()

        width = 0.7
        labels_x = list(map(lambda x: x[0], skills_arr))
        data = list(map(lambda x: x[1], skills_arr))
        points = range(len(labels_x))

        ax.bar(points, data, width)
        ax.set_title(f'Навыки за {year} год')
        ax.grid(axis='y')

        for label in ax.get_yticklabels():
            label.set_fontsize(8)

        ax.set_xticks(points, labels_x, fontsize=8, rotation=90)

        fig.tight_layout()
        fig.set_size_inches(8, 6)
        fig.set_dpi(300)
        fig.savefig(f'skills_images/{year}.png', dpi=300)

        plt.show()

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
    salaries_vac = {'2003': 30318, '2004': 30209, '2005': 32089, '2006': 40923, '2007': 41119, '2008': 41776, '2009': 41269, '2010': 44884, '2011': 44970, '2012': 50454, '2013': 45528, '2014': 51206, '2015': 55777, '2016': 58280, '2017': 63581, '2018': 68357, '2019': 74418, '2020': 79103, '2021': 95131, '2022': 101579}
    count = {'2003': 1983, '2004': 7833, '2005': 16022, '2006': 33321, '2007': 53562, '2008': 75070, '2009': 52889, '2010': 93494, '2011': 142458, '2012': 173897, '2013': 234019, '2014': 259571, '2015': 284763, '2016': 332460, '2017': 391464, '2018': 517670, '2019': 535956, '2020': 489472, '2021': 287915, '2022': 91142}
    count_vac = {'2003': 14, '2004': 63, '2005': 154, '2006': 568, '2007': 871, '2008': 1216, '2009': 1012, '2010': 1678, '2011': 3094, '2012': 3396, '2013': 5025, '2014': 4791, '2015': 5699, '2016': 7606, '2017': 8570, '2018': 9434, '2019': 7992, '2020': 5850, '2021': 2746, '2022': 690}
    area_sal = [('Киев', 83426), ('Москва', 79975), ('Минск', 67968), ('Санкт-Петербург', 67448), ('Новосибирск', 63658), ('Екатеринбург', 59426), ('Самара', 54982), ('Краснодар', 53836), ('Челябинск', 52650), ('Пермь', 52540)]
    area_count = [('Москва', 0.2501809306219756), ('Санкт-Петербург', 0.11572464487930863), ('Минск', 0.04010274021200812), ('Киев', 0.03354666590983269), ('Алматы', 0.028934708879081582), ('Нижний Новгород', 0.02628105975677248), ('Новосибирск', 0.02469170841079056), ('Ростов-на-Дону', 0.019767557365650144), ('Краснодар', 0.01951212589933162), ('Казань', 0.019029644240729966)]
    skills = {'2015': [('JavaScript', 699), ('PHP', 696), ('HTML', 553), ('MySQL', 509), ('CSS', 499), ('HTML5', 479), ('jQuery', 456), ('CSS3', 421), ('Ajax', 377), ('PHP5', 311)], '2016': [('JavaScript', 1958), ('PHP', 1737), ('HTML', 1473), ('CSS', 1293), ('jQuery', 1289), ('MySQL', 1289), ('HTML5', 1176), ('CSS3', 1001), ('PHP5', 782), ('Git', 762)], '2017': [('JavaScript', 2882), ('PHP', 2575), ('HTML', 2143), ('CSS', 2103), ('MySQL', 2014), ('jQuery', 1835), ('HTML5', 1539), ('Git', 1214), ('CSS3', 1111), ('1С-Битрикс', 1045)], '2018': [('JavaScript', 3434), ('PHP', 3192), ('HTML', 2614), ('MySQL', 2494), ('CSS', 2484), ('jQuery', 2162), ('HTML5', 1837), ('Git', 1557), ('CSS3', 1353), ('1С-Битрикс', 1178)], '2019': [('JavaScript', 3333), ('PHP', 2806), ('HTML', 2545), ('CSS', 2453), ('MySQL', 2084), ('jQuery', 1980), ('HTML5', 1564), ('Git', 1530), ('CSS3', 1193), ('1С-Битрикс', 1169)], '2020': [('JavaScript', 3146), ('PHP', 2459), ('CSS', 2222), ('HTML', 2162), ('MySQL', 2143), ('jQuery', 1715), ('Git', 1678), ('HTML5', 1195), ('1С-Битрикс', 1048), ('CSS3', 931)], '2021': [('JavaScript', 1555), ('PHP', 1170), ('CSS', 1076), ('MySQL', 1014), ('HTML', 1006), ('Git', 848), ('jQuery', 760), ('HTML5', 530), ('1С-Битрикс', 480), ('CSS3', 432)], '2022': [('PHP', 396), ('JavaScript', 356), ('HTML', 272), ('MySQL', 268), ('CSS', 256), ('Git', 218), ('jQuery', 161), ('ООП', 155), ('HTML5', 125), ('1С-Битрикс', 122)]}


    s_all = {}
    s_filtered = {}

    for year in salaries.keys():
        s_all[year] = [salaries[year], count[year]]
        s_filtered[year] = [salaries_vac[year], count_vac[year]]

    image_generator = Graph('Web-программист')

    for key in skills.keys():
        image_generator.draw_skills(skills[key], key)

    image_generator.draw(
        s_all,
        s_filtered,
        area_count,
        area_sal
    )