"""
This script runs the application using a development server.
"""

import bottle
import os
import sys
from articles_load import load_articles

import routes

if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
    bottle.debug(True)

bottle.default_app().merge(routes.app)

def wsgi_app():
    """Returns the application to make available through wfastcgi."""
    return bottle.default_app()

# Страница со статьями
@bottle.route('/articles')
def articles():
    data = load_articles()
    articles = data.get('articles', []) if 'articles' in data else []
    error = data.get('error', None)
    return bottle.template('articles', title='Useful articles', year=2025, articles=articles, error=error)

if __name__ == '__main__':
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    @bottle.route('/static/<filepath:path>')
    def server_static(filepath):
        return bottle.static_file(filepath, root=STATIC_ROOT)
      
    bottle.run(server='wsgiref', host=HOST, port=PORT