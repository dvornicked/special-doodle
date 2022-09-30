import unittest
from main import CashCalculator, CaloriesCalculator, Record


class TestCalcs(unittest.TestCase):
    def test_cashCalc(self):
        cash_calculator = CashCalculator(1000)
        cash_calculator.add_record(Record(amount=145, comment='кофе'))
        cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
        cash_calculator.add_record(Record(amount=3000, comment='бар в Танин др'))
        self.assertEqual(cash_calculator.get_today_cash_remained('rub'), 'Your debt is -2445.0 Rub')

    def test_CalCalc(self):
        calories_calculator = CaloriesCalculator(2000)
        calories_calculator.add_record(Record(amount=1186, comment='Кусок тортика. И ещё один.'))
        calories_calculator.add_record(Record(amount=84, comment='Йогурт.', ))
        calories_calculator.add_record(Record(amount=1140, comment='Баночка чипсов.', ))
        self.assertEqual(calories_calculator.get_calories_remained(), 'Stop eating for today')


if __name__ == '__main__':
    unittest.main()
