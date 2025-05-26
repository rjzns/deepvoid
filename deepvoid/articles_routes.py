import bottle
from articles_load import load_articles
from articles_add import add_article

# Страница со статьями
@bottle.route('/articles', method=['GET', 'POST'])
def articles():
    message = None  # Для хранения сообщения при добавлении

    if bottle.request.method == 'POST':
        # Получение данных из формы
        title = bottle.request.forms.get('title')
        author = bottle.request.forms.get('author')
        description = bottle.request.forms.get('description')
        link = bottle.request.forms.get('link')
        
        # Добавление статьи
        success = add_article(title, author, description, link)
        
        if success:
            message = "Article added successfully"
        else:
            message = "Failed to add article. Please try again"
    
    # Загрузка статей (либо после добавления, либо при GET-запросе)
    data = load_articles()
    # Проверка, что data — это словарь, и articles — список
    if not isinstance(data, dict):
        data = {'error': 'Invalid data format from load_articles', 'articles': []}
    articles = data.get('articles', []) if 'articles' in data else []
    error = data.get('error', None)
    # Рендер шаблона с обновлёнными данными
    return bottle.template('articles', title='Useful articles', year=2025, articles=articles, error=error, message=message)