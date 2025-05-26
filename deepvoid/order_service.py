# Импортируются необходимые модули для работы с JSON, файловой системой, датами и регулярными выражениями
import json
import os
from datetime import datetime
import re

# Определяется путь к файлу для хранения заказов
DATA_FILE = 'data/orders.json'

# Задается словарь с ценами на услуги
SERVICE_PRICES = {
    'sound_equipment': 15000,
    'light_equipment': 10000,
    'stage_structures': 20000,
    'special_effects': 12000,
    'technical_support': 25000
}

# Задается словарь с отображаемыми именами услуг
SERVICE_NAMES = {
    'sound_equipment': 'Sound Equipment Rental',
    'light_equipment': 'Light Equipment Rental',
    'stage_structures': 'Stage Structures Rental',
    'special_effects': 'Special Effects Equipment Rental',
    'technical_support': 'Technical Event Support'
}

# Определяется функция для загрузки списка заказов из файла
def load_orders():
    # Проверяется существование файла с заказами
    if not os.path.exists(DATA_FILE):
        # Возвращается пустой список, если файл не существует
        return []
    # Открывается файл для чтения с кодировкой UTF-8
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        # Загружаются данные из JSON-файла
        return json.load(f)

# Определяется функция для генерации номера заказа
def generate_order_number():
    # Загружается список существующих заказов
    orders = load_orders()
    # Формируется номер заказа в формате ORD-XXX
    return f"ORD-{len(orders) + 1:03d}"

# Определяется функция для расчета общей стоимости услуг
def calculate_total_amount(services):
    # Суммируются цены выбранных услуг, если услуга отсутствует, используется 0
    return sum(SERVICE_PRICES.get(service, 0) for service in services)

# Определяется функция для сохранения заказа
def save_order(order):
    # Загружается список существующих заказов
    orders = load_orders()
    # Добавляется временная метка к заказу
    order['timestamp'] = datetime.now().isoformat()
    # Новый заказ добавляется в начало списка
    orders.insert(0, order)
    # Открывается файл для записи с кодировкой UTF-8
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        # Сохраняются данные в JSON-файл с форматированием
        json.dump(orders, f, ensure_ascii=False, indent=4)

# Определяется функция для валидации данных заказа
def validate_order(data):
    # Создается словарь для хранения ошибок валидации
    errors = {}
    # Получаются данные из входного словаря с удалением пробелов
    name = data.get("name", "").strip()
    services = data.get("services", [])
    description = data.get("description", "").strip()
    date = data.get("date", "")
    phone = data.get("phone", "").strip()

    # Проверяется поле имени
    # Проверяется, не пустое ли имя
    if not name:
        errors["name"] = "Please enter your name."
    # Проверяется, не состоит ли имя только из пробелов
    elif name.isspace():
        errors["name"] = "Name cannot consist of only whitespace."
    # Проверяется минимальная длина имени
    elif len(name) < 2:
        errors["name"] = "Name must be at least 2 characters long."
    # Проверяется максимальная длина имени
    elif len(name) > 100:
        errors["name"] = "Name cannot exceed 100 characters."
    # Проверяется, содержит ли имя только допустимые символы
    elif not re.match(r"^[a-zA-Zа-яА-Я\s-]+$", name):
        errors["name"] = "Name can only contain letters, spaces, and hyphens."

    # Проверяется наличие выбранных услуг
    if not services:
        errors["services"] = "Please select at least one service."
    # Проверяется наличие описания
    if not description:
        errors["description"] = "Please enter a description."
    # Проверяется наличие даты
    if not date:
        errors["date"] = "Please enter a date."
    else:
        # Проверяется наличие пробелов в начале или конце даты
        if date != date.strip():
            errors["date"] = "Date must not contain leading or trailing whitespace."
        else:
            # Определяется шаблон для проверки формата даты
            date_pattern = r"^\d{2}\.\d{2}\.\d{4}$"
            # Проверяется соответствие даты формату DD.MM.YYYY
            if not re.match(date_pattern, date):
                errors["date"] = "Date must be in format DD.MM.YYYY."
            else:
                try:
                    # Преобразуется строка даты в объект datetime
                    order_date = datetime.strptime(date, "%d.%m.%Y")
                    # Получается текущая дата
                    current_date = datetime.now()
                    # Проверяется, что дата заказа в будущем
                    if order_date.date() <= current_date.date():
                        errors["date"] = "Date must be in the future."
                except ValueError:
                    # Обрабатывается ошибка неверного формата даты
                    errors["date"] = "Invalid date format."
    # Проверяется формат номера телефона, если он указан
    if phone and not re.match(r"^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$", phone):
        errors["phone"] = "Phone must be in format +7(XXX)XXX-XX-XX."

    # Возвращается словарь с ошибками валидации
    return errors