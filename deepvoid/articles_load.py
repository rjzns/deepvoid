import json

def load_articles():
    try:
        # Попытка открыть файл './static/texts/articles.json' в режиме чтения ('r') с кодировкой UTF-8.
        with open('./static/texts/articles.json', 'r', encoding='utf-8') as file:
            articles = json.load(file) # Чтение содержимого файла и преобразование JSON-данных в объект Python
        # Если файл успешно прочитан, возвращается словарь с ключом 'articles'
        return {'articles': articles}
    except Exception as e:
        return {'error': str(e)}