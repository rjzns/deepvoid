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

def check_title(title):
    # Проверка длины (не больше 255)
    if len(title) > 255:
        return "The title must not exceed 255 characters."
    
    # Проверка на допустимые символы (англ буквы, цифры, - . , ; : ! ? " & № % ())
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9\-\.\,\;\:\!\?\"\&\№\%\(\) ]*$', title):
        if not title[0].isalpha():
            return "The title must begin with the letter"
        return "The title can contain only English letters, numbers, and symbols: - . , ; : ! ? \" & № % ( )"
    
    # Проверка на повторение специальных символов
    special_chars = r'[\-\.\,\;\:\!\?\"\&\№\%\(\)]' # Все специальные символы из допустимого набора
    # Проверка на повторение подряд
    if re.search(r'([\-,;:!?\"&№%()])\1', title):
        return "The title may not contain several special characters in a row"
    # Проверяем повторение через пробел, исключая случаи вроде ", -"
    if re.search(r'([\-,\.;:!?\"&№%()])\s*\1', title) and not re.search(r'[,\.;:!?]\s{1}\-|[\.\?!]\s*$|\"\.?|\"!|\"?', title):
        return "The title may not contain several special characters in a row"
    
    # Подсчёт буквенных символов
    letter_count = len(re.findall(r'[a-zA-Z]', title))
    if letter_count < 4:
        return "The title must contain at least 4 letters."
    
    return True

def check_author(author): 
    # Проверка длины (не больше 255)
    if len(author) > 255:
        return "The author's name must not exceed 255 characters"
    
    # Проверка на допустимые символы (англ буквы, -)
    if not re.match(r'^[a-zA-Z][a-zA-Z\-]*$', author):
        if author.startswith('-'):
            return "The author's name cannot begin with -"
        return "The author's name can contain only English letters and a symbol -"
    
    # Проверка на несколько - рядом (включая через пробел)
    if re.search(r'\-[\s\-]*\-', author):
        return "The author's name cannot contain several - in a row"
    
    # Подсчёт буквенных символов
    letter_count = len(re.findall(r'[a-zA-Z]', author))
    if letter_count < 4:
        return "The author's name must contain at least 4 letters"
    
    return True

def check_description(description):
    # Проверка длины (не больше 1023)
    if len(description) > 1023:
        return "The description must not exceed 1023 characters"
    
    # Проверка на допустимые символы (англ буквы, цифры,  - . , ; : ! ? " & № % ())
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9\-\.\,\;\:\!\?\"\&\№\%\(\) ]*$', description):
        if not description[0].isalpha():
            return "The description must begin with the letter"
        return "The description can contain only English letters, numbers, and symbols: - . , ; : ! ? \" & № % ( )"
    
    # Проверка на повторение специальных символов
    special_chars = r'[\-\.\,\;\:\!\?\"\&\№\%\(\)]' # Все специальные символы из допустимого набора
    # Проверяем повторение подряд
    if re.search(r'([\-,;:!?\"&№%()])\1', description):
        return "The description cannot contain several special characters in a row."
    # Проверяем повторение через пробел, исключая случаи вроде ", -"
    if re.search(r'([\-,\.;:!?\"&№%()])\s*\1', description) and not re.search(r'[,\.;:!?]\s{1}\-|[\.\?!]\s*$|\"\.?|\"!|\"?', description):
        return "The description cannot contain several special characters in a row."
        
    # Подсчёт буквенных символов
    letter_count = len(re.findall(r'[a-zA-Z]', description))
    if letter_count < 20:
        return "The description must contain at least 20 letters"
    
    return True

def add_article(title, author, description, link):
    try:
        # Чтение текущих статей из файла
        try:
            with open('./static/texts/articles.json', 'r', encoding='utf-8') as file:
                articles = json.load(file)
        except FileNotFoundError:
            articles = []  # Если файла нет, начинаем с пустого списка
        
        # Проверка каждого поля и сбор ошибок
        errors = {}
        title_result = check_title(title)
        if title_result is not True:
            errors['title'] = title_result
        
        author_result = check_author(author)
        if author_result is not True:
            errors['author'] = author_result
        
        description_result = check_description(description)
        if description_result is not True:
            errors['description'] = description_result
        
        # Если есть ошибки, возвращаем их
        if errors:
            return {'success': False, 'errors': errors}

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

        # Приведение всех дат к единому формату перед сортировкой
        for article in articles:
            article['date'] = normalize_date(article['date'])
        
        # Сортировка статей: сначала по дате (убывание), затем по названию (возрастание), затем по автору (возрастание)
        articles.sort(key=lambda x: (-datetime.strptime(x['date'], "%Y-%m-%d").timestamp(), x['title'].lower(), x['author'].lower()))
        
        # Сохранение обновлённого и отсортированного списка обратно в файл
        with open('./static/texts/articles.json', 'w', encoding='utf-8') as file:
            json.dump(articles, file, ensure_ascii=False, indent=2)
        
        return {'success': True} # Успешно добавлено
    except Exception as e:
        return {'success': False, 'errors': {'general': f"Error adding an article: {str(e)}"}}