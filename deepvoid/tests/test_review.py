import unittest
from review_service import validate_review

class TestPhoneValidation(unittest.TestCase):

    def test_valid_phone_numbers(self):
        valid_phones = [
            "+7(911)746-43-56",
            "+7(495)123-45-67",
            "+7(800)555-35-35",
            "+7(999)999-99-99",
            "+7(123)456-78-90",
            "+7(321)654-32-10",
            "+7(000)000-00-00",
            "+7(987)654-32-10",
            "+7(701)111-11-11",
            "+7(777)777-77-77",
            "+7(812)312-12-12",
            "+7(111)111-11-11"
        ]

        for phone in valid_phones:
            with self.subTest(phone=phone):
                data = {"author": "Tester", "text": "Some review", "phone": phone}
                errors = validate_review(data)
                self.assertNotIn("phone", errors, f"Phone '{phone}' should be valid")

    def test_invalid_phone_numbers(self):
        invalid_phones = [
            "89117464356",
            "+7 911 746 43 56",
            "+7-911-746-43-56",
            "+7(911)7464356",
            "+7(911)746-4356",
            "+7(911746-43-56",
            "7(911)746-43-56",
            "+7(911)746-43-5",
            "+7(91)1746-43-56", 
            "+7(911)7463-456",
            "+8(911)746-43-56",
            "qwe"
        ]

        for phone in invalid_phones:
            with self.subTest(phone=phone):
                data = {"author": "Tester", "text": "Some review", "phone": phone}
                errors = validate_review(data)
                self.assertIn("phone", errors, f"Phone '{phone}' should be invalid")

if __name__ == '__main__':
    unittest.main()

