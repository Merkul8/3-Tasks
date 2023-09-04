import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import unquote

alph = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ'

# Создаем словарь для подсчета количества животных по буквам
animal_counts = {letter: 0 for letter in alph}

for letter in alph:
    url = f"https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&from={letter}"

    response = requests.get(url)
    page_content = response.content

    soup = BeautifulSoup(page_content, "lxml")
    # Получаем div со всеми ссылками
    main_div = soup.find('div', attrs={'class':'mw-category-columns'})
    # Находим эти ссылки
    links = main_div.find_all('a')
    for link in links:
        animal_counts[letter] += 1

# Записываем результат в CSV-файл
with open('beasts.csv', mode='w', encoding='cp1251', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Буква', 'Количество'])
    for letter, count in animal_counts.items():
        writer.writerow([letter, count])
