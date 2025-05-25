# -*- coding: utf-8 -*-
"""
Routes and views for the bottle application.
"""

from bottle import Bottle, route, view, request, template, redirect, static_file, run
from datetime import datetime
import review_service
import order_service

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

@app.route('/orders', method=['GET', 'POST'])
def orders():
    errors = {}

    if request.method == 'POST':
        # Получаем данные из формы
        data = {
            "name": request.forms.get('name', '').strip(),
            "services": request.forms.getall('services') or [],
            "description": request.forms.get('description', '').strip(),
            "date": request.forms.get('date', '').strip(),
            "phone": request.forms.get('phone', '').strip(),
            "total_amount": int(request.forms.get('total_amount', '0') or 0)
        }

        # Валидация
        errors = order_service.validate_order(data)

        # Если всё корректно — сохраняем и редирект
        if not errors:
            order = {
                "order_number": order_service.generate_order_number(),
                "name": data["name"],
                "services": data["services"],
                "description": data["description"],
                "date": data["date"],
                "phone": data["phone"],
                "total_amount": data["total_amount"],
                "timestamp": datetime.now().isoformat()
            }
            order_service.save_order(order)
            redirect('/orders')
    else:
        # Для GET-запроса — пустые поля
        data = {
            "name": "",
            "services": [],  # ❗ по умолчанию ничего не выбрано
            "description": "",
            "date": "",
            "phone": "",
            "total_amount": 0
        }

    orders = order_service.load_orders()

    return template(
        'orders',
        orders=orders,
        data=data,
        errors=errors,
        year=datetime.now().year,
        title="Orders",
        SERVICE_NAMES=[
            ("sound_equipment", "Sound Equipment Rental (15,000 ₽)"),
            ("light_equipment", "Light Equipment Rental (10,000 ₽)"),
            ("stage_structures", "Stage Structures Rental (20,000 ₽)"),
            ("special_effects", "Special Effects Equipment Rental (12,000 ₽)"),
            ("technical_support", "Technical Event Support (25,000 ₽)")
        ],
        request=request
    )
