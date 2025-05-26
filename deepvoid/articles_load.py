import json

def load_articles():
    try:
        # ������� ������� ���� './static/texts/articles.json' � ������ ������ ('r') � ���������� UTF-8.
        with open('./static/texts/articles.json', 'r', encoding='utf-8') as file:
            articles = json.load(file) # ������ ����������� ����� � �������������� JSON-������ � ������ Python
        # ���� ���� ������� ��������, ������������ ������� � ������ 'articles'
        return {'articles': articles}
    except Exception as e:
        return {'error': str(e)}