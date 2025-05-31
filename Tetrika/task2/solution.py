import csv

import wikipediaapi
from collections import Counter

wiki_wiki = wikipediaapi.Wikipedia(
    user_agent='MyProjectName (merlin@example.com)',
    language='ru',
    extract_format=wikipediaapi.ExtractFormat.WIKI
)


def get_categorymembers(categorymembers, level=0, max_level=1):
    lst = []
    for c in categorymembers.values():
        lst.append(c.title[0])
        if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
            get_categorymembers(c.categorymembers, level=level + 1, max_level=max_level)
    return Counter(lst)


page_py = wiki_wiki.page('Категория:Животные_по_алфавиту')
print(get_categorymembers(page_py.categorymembers))


def write_data(data):
    try:
        with open("beasts.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(['Буква', 'Количество'])
            for alph, count in data.items():
                writer.writerow([alph, count])
        print("Данные успешно записаны")
    except Exception as e:
        print(e)


write_data(get_categorymembers(page_py.categorymembers))
