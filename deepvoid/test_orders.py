import unittest
from datetime import datetime, timedelta
from order_service import validate_order  # Replace with actual module name

class TestDateValidation(unittest.TestCase):

    def test_valid_dates(self):
        # Generate future dates for testing (after May 26, 2025)
        current_date = datetime.now()
        tomorrow = (current_date + timedelta(days=1)).strftime("%d.%m.%Y")
        next_week = (current_date + timedelta(days=7)).strftime("%d.%m.%Y")
        next_month = (current_date + timedelta(days=30)).strftime("%d.%m.%Y")
        next_year = (current_date + timedelta(days=365)).strftime("%d.%m.%Y")
        
        valid_dates = [
            tomorrow,
            next_week,
            next_month,
            next_year,
            "27.05.2025",  # Day after current date
            "31.12.2025",  # End of 2025
            "15.06.2026",  # Mid-2026
            "29.02.2028",  # Valid leap year date
            "01.01.2030",  # Far future
            "10.10.2025",  # Later in 2025
        ]

        for date in valid_dates:
            with self.subTest(date=date):
                data = {
                    "name": "Tester",
                    "services": ["sound_equipment"],
                    "description": "Event description",
                    "date": date,
                    "phone": "+7(911)746-43-56"
                }
                errors = validate_order(data)
                self.assertNotIn("date", errors, f"Date '{date}' should be valid")

    def test_invalid_dates(self):
        # Generate past and current dates for testing
        past_date = (datetime.now() - timedelta(days=1)).strftime("%d.%m.%Y")
        current_date = datetime.now().strftime("%d.%m.%Y")
        
        invalid_dates = [
            "",  # Empty date
            "01.01.2025",  # Past date
            current_date,  # Current date (now invalid)
            " 01.01.2026 ",  # Whitespace (now invalid)
            "2023-12-25",  # Wrong format (ISO)
            "25/12/2025",  # Wrong separator
            "25.12.25",  # Short year
            "32.12.2025",  # Invalid day
            "00.12.2025",  # Zero day
            "31.13.2025",  # Invalid month
            "31.04.2025",  # April has 30 days
            "29.02.2025",  # Non-leap year
            "abc",  # Non-date string
            "1.1.2025",  # Missing leading zeros
            "01.01.202",  # Incomplete year
            "01-01-2025",  # Wrong separator
            "15.15.2025",  # Invalid month
            "01.01.20 25",  # Space in year
            "31.12.2024",  # Past date (end of 2024)
            " 27.05.2025",  # Leading whitespace
            "27.05.2025 ",  # Trailing whitespace
        ]

        for date in invalid_dates:
            with self.subTest(date=date):
                data = {
                    "name": "Tester",
                    "services": ["sound_equipment"],
                    "description": "Event description",
                    "date": date,
                    "phone": "+7(911)746-43-56"
                }
                errors = validate_order(data)
                self.assertIn("date", errors, f"Date '{date}' should be invalid")

if __name__ == '__main__':
    unittest.main()