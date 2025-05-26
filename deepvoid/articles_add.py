import json
from datetime import datetime
import re

def normalize_date(date_str):
    try:
        # Проверяем, соответствует ли строка формату DD.MM.YYYY
        if re.match(r'\d{2}\.\d{2}\.\d{4}', date_str):
            return datetime.strptime(date_str, "%d.%m.%Y").strftime("%Y-%m-%d")
        # Если уже в формате YYYY-MM-DD, возвращаем как есть
        elif re.match(r'\d{4}-\d{2}-\d{2}', date_str):
            return date_str
        # Если формат неизвестный, возвращаем текущую дату
        return datetime.now().strftime("%Y-%m-%d")
    except ValueError:
        # Если не удалось распарсить, возвращаем текущую дату
        return datetime.now().strftime("%Y-%m-%d")

def add_article(title, author, description, link):
    try:
        # Чтение текущих статей из файла
        try:
            with open('./static/texts/articles.json', 'r', encoding='utf-8') as file:
                articles = json.load(file)
        except FileNotFoundError:
            articles = []  # Если файла нет, начинаем с пустого списка
        
        # Формирование новой статьи
        new_article = {
            "title": title,
            "author": author,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d"),  # Текущая дата в формате YYYY-MM-DD
            "link": link
        }
        
        # Добавление новой статьи в список
        articles.append(new_article)

        # Приводим все даты к единому формату перед сортировкой
        for article in articles:
            article['date'] = normalize_date(article['date'])
        
        # Сортировка статей: сначала по дате (убывание), затем по названию (возрастание), затем по автору (возрастание)
        articles.sort(key=lambda x: (-datetime.strptime(x['date'], "%Y-%m-%d").timestamp(), x['title'].lower(), x['author'].lower()))
        
        # Сохранение обновлённого и отсортированного списка обратно в файл
        with open('./static/texts/articles.json', 'w', encoding='utf-8') as file:
            json.dump(articles, file, ensure_ascii=False, indent=2)
        
        return True  # Успешно добавлено
    except Exception as e:
        print(f"Ошибка при добавлении статьи: {str(e)}")
        return False  # Ошибка при добавлении