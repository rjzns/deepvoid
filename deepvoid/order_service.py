import json
import os
from datetime import datetime
import re

DATA_FILE = 'data/orders.json'

# Service prices and display names
SERVICE_PRICES = {
    'sound_equipment': 15000,
    'light_equipment': 10000,
    'stage_structures': 20000,
    'special_effects': 12000,
    'technical_support': 25000
}

SERVICE_NAMES = {
    'sound_equipment': 'Sound Equipment Rental',
    'light_equipment': 'Light Equipment Rental',
    'stage_structures': 'Stage Structures Rental',
    'special_effects': 'Special Effects Equipment Rental',
    'technical_support': 'Technical Event Support'
}

def load_orders():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_order_number():
    orders = load_orders()
    return f"ORD-{len(orders) + 1:03d}"

def calculate_total_amount(services):
    return sum(SERVICE_PRICES.get(service, 0) for service in services)

def save_order(order):
    orders = load_orders()
    order['timestamp'] = datetime.now().isoformat()
    orders.insert(0, order)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(orders, f, ensure_ascii=False, indent=4)

def validate_order(data):
    errors = {}
    name = data.get("name", "").strip()
    services = data.get("services", [])
    description = data.get("description", "").strip()
    date = data.get("date", "").strip()
    phone = data.get("phone", "").strip()

    if not name:
        errors["name"] = "Please enter your name."
    if not services:
        errors["services"] = "Please select at least one service."
    if not description:
        errors["description"] = "Please enter a description."
    if not date:
        errors["date"] = "Please enter a date."
    else:
        date_pattern = r"^\d{2}\.\d{2}\.\d{4}$"
        if not re.match(date_pattern, date):
            errors["date"] = "Date must be in format DD.MM.YYYY."
        else:
            try:
                order_date = datetime.strptime(date, "%d.%m.%Y")
                current_date = datetime.now()
                if order_date.date() < current_date.date():
                    errors["date"] = "Date cannot be in the past."
            except ValueError:
                errors["date"] = "Invalid date format."
    if phone and not re.match(r"^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$", phone):
        errors["phone"] = "Phone must be in format +7(XXX)XXX-XX-XX."

    return errors