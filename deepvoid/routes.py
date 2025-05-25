# -*- coding: utf-8 -*-
"""
Routes and views for the bottle application.
"""

from bottle import Bottle, route, view, request, template, redirect, static_file, run
from datetime import datetime
import review_service

app = Bottle()

@app.route('/')
@app.route('/home')
@view('index')
def home():
    return dict(
        year=datetime.now().year
    )

@app.route('/service')
@view('service')
def service():
    return dict(
        title='Services',
        message='Наши услуги',
        year=datetime.now().year
    )

@app.route('/about')
@view('about')
def about():
    return dict(
        title="О нас",
        message="Предоставление аренды звукового и светового оборудования для ночных клубов",
        year=datetime.now().year
    )

from bottle import route, request, redirect, template, static_file
from datetime import datetime
import review_service

@app.route('/static/<filename>')
def send_static(filename):
    return static_file(filename, root='static')

@app.route('/reviews', method=['GET', 'POST'])
def reviews():
    errors = {}
    data = {
        "author": "",
        "text": "",
        "phone": ""
    }

    if request.method == 'POST':
        data["author"] = request.forms.get('author', '').strip()
        data["text"] = request.forms.get('text', '').strip()
        data["phone"] = request.forms.get('phone', '').strip()

        errors = review_service.validate_review(data)

        if not errors:
            review = {
                "author": data["author"],
                "text": data["text"],
                "phone": data["phone"]
            }
            review_service.save_review(review)
            redirect('/reviews')

    reviews = review_service.load_reviews()
    return template('reviews', reviews=reviews, data=data, errors=errors, year=datetime.now().year, title="Reviews")