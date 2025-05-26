import json

def load_articles():
    try:
        with open('./static/texts/articles.json', 'r', encoding='utf-8') as file:
            articles = json.load(file)
        return {'articles': articles}
    except Exception as e:
        return {'error': str(e)}