# -*- coding: utf-8 -*-
"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/service')
@view('service')
def contact():
    """Renders the contact page."""
    return dict(
        title='Services',
        message='Наши услуги совсем скоро',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title="О нас",
        message="Предоставление аренды звукового и светового оборудования для ночных клубов",
        year=datetime.now().year
    )
