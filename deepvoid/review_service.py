import json
import os
from datetime import datetime

DATA_FILE = 'data/reviews.json'

def load_reviews():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_review(review):
    reviews = load_reviews()
    # Add timestamp automatically
    review['timestamp'] = datetime.now().isoformat()
    reviews.insert(0, review)  # Add new review to the top
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(reviews, f, ensure_ascii=False, indent=4)

def validate_review(data):
    errors = {}
    author = data.get("author", "").strip()
    text = data.get("text", "").strip()

    if not author:
        errors["author"] = "Please enter your name or nickname."
    if not text:
        errors["text"] = "Please enter your review text."

    return errors
