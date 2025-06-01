import unittest
from articles_add import check_title

# Успешные случаи — заголовки, которые должны пройти проверку
valid_titles = [
    {'title': 'Simple Title'},  # Простой заголовок только с буквами и пробелом
    {'title': 'Title123'},  # Заголовок с цифрами
    {'title': 'Hello, -World'},  # Допустимая пунктуация: запятая, пробел, дефис
    {'title': 'Event №1'},  # Использование символа №
    {'title': 'Special (Offer)'},  # Использование скобок
    {'title': 'Get 10% Off'},  # Использование процента
    {'title': 'Quote: "Hello"!'},  # Кавычки с восклицательным знаком
    {'title': 'Multiple symbols: (Yes)! And & 100% more.'},  # Комбинации символов
    {'title': 'Long but valid title ' + 'A' * 230},  # ~255 символов
]

# Неуспешные случаи — заголовки, которые должны вызвать ошибку
invalid_titles = [
    {
        # Начинается не с буквы
        'title': '123Title', 
        'expected_error': 'The title must begin with the letter'
    },  
    {
        # Меньше 4 букв
        'title': 'Hi', 
        'expected_error': 'The title must contain at least 4 letters'
    },  
    {
        # Длина больше 255 символов
        'title': 'A' * 256, 
        'expected_error': 'The title must not exceed 255 characters'
    },  
    {
        # Повторяющиеся запятные
        'title': 'Hello,,World', 
        'expected_error': 'The title may not contain several special characters in a row'
    },  
    {
        # Повторяющиеся дефисы через пробел
        'title': 'Hello - - World', 
        'expected_error': 'The title may not contain several special characters in a row'
    },  
    {
        # Повторяющиеся амперсанды
        'title': 'Hello&&World', 
        'expected_error': 'The title may not contain several special characters in a row'
    },  
    {
        # Недопустимый символ /
        'title': 'Hello/World', 
        'expected_error': 'The title can contain only English letters, numbers, and symbols: - . , ; : ! ? \" & № % ( )'
    },  
    {
        # Повторяющиеся дефисы подряд
        'title': 'Hello--World', 
        'expected_error': 'The title may not contain several special characters in a row'
    },  
    {
        'title': 'No l 123',
        'expected_error': 'The title must contain at least 4 letters'
    }
]

class TestCheckTitle(unittest.TestCase):
    def test_valid_titles(self):
        # Тестировка успешных случаев
        for case in valid_titles:
            with self.subTest(case=case):
                result = check_title(case['title'])
                # Проверяка, что функция возвращает True
                self.assertTrue(result, f"Ожидалось, что заголовок '{case['title']}' валиден, но получена ошибка: {result}")

    def test_invalid_titles(self):
        # Тестировка неуспешных случаев
        for case in invalid_titles:
            with self.subTest(case=case):
                result = check_title(case['title'])
                # Проверка, что функция возвращает ожидаемую строку ошибки
                self.assertEqual(result, case['expected_error'], 
                                f"Для заголовка '{case['title']}' ожидалась ошибка '{case['expected_error']}', но получено: {result}")

if __name__ == '__main__':
    # Запуск тестов с подробным выводом
    unittest.main(verbosity=3)