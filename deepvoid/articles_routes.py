import bottle
from articles_load import load_articles
from articles_add import add_article

# Страница со статьями
@bottle.route('/articles', method=['GET', 'POST'])
def articles():
    # Статьи для отображения
    data = load_articles()
    articles = data.get('articles', []) if 'articles' in data else []
    error = data.get('error', None)

    # Ошибки для формы (по умолчанию пустой словарь)
    form_errors = {}

    form_data = {'title': '', 'author': '', 'description': '', 'link': ''}  # Значения по умолчанию

    if bottle.request.method == 'POST':
        # Получение данных из формы
        title = bottle.request.forms.get('title')
        author = bottle.request.forms.get('author')
        description = bottle.request.forms.get('description')
        link = bottle.request.forms.get('link')

        # Сохранение введённых данных, чтобы вернуть в шаблон при ошибках
        form_data = {
            'title': title,
            'author': author,
            'description': description,
            'link': link
        }
        
        # Добавление статьи
        result = add_article(title, author, description, link)
        
        if result['success']:
            # Если успешно, перенаправление на ту же страницу, чтобы обновить таблицу
            form_data = {'title': '', 'author': '', 'description': '', 'link': ''}
            form_errors = {}
            data = load_articles()
            articles = data.get('articles', [])
        else:
            # Если есть ошибки, передача их в шаблон
            form_errors = result.get('errors', {})
    
    return bottle.template('articles', 
                           title='Useful articles', 
                           year=2025, articles=articles, 
                           error=error, 
                           form_errors=form_errors,
                           form_data=form_data)