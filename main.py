import datetime as dt


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.today = dt.date.today()
        self.week_ago = self.today - dt.timedelta(7)

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        return sum([record.amount if record.date == self.today else 0 for record in self.records])

    def get_week_stats(self):
        return sum([record.amount if self.week_ago <= record.date <= self.today else 0 for record in self.records])

    def get_today_limit_balance(self):
        print(self.get_today_stats())
        return self.limit - self.get_today_stats()


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_remained = self.get_today_limit_balance()
        return f'You can still eat {calories_remained} calories' if calories_remained > 0 else 'Stop eating for today'


class CashCalculator(Calculator):
    USD_RATE = 57.50
    EURO_RATE = 56.42
    RUB_RATE = 1

    def get_today_cash_remained(self, currency='rub'):
        currencies = {'usd': ('USD', CashCalculator.USD_RATE), 'eur': ('Euro', CashCalculator.EURO_RATE),
                      'rub': ('Rub', CashCalculator.RUB_RATE)}

        cash_remained = self.get_today_limit_balance()
        if cash_remained == 0:
            return 'There is no money, but you hold on! - D. Medvedev'

        if currency not in currencies:
            return f'Currency {currency} not supported'

        name, rate = currencies[currency]
        cash_remained = round(cash_remained / rate, 2)
        return f'{cash_remained} {name} left' if cash_remained > 0 else f'Your debt is {cash_remained} {name}'


# Ctrl + C & Ctrl + V
calories_calculator = CaloriesCalculator(2000)
calories_calculator.add_record(Record(amount=1186, comment='Кусок тортика. И ещё один.'))
calories_calculator.add_record(Record(amount=84, comment='Йогурт.', ))
calories_calculator.add_record(Record(amount=1140, comment='Баночка чипсов.', ))
print(calories_calculator.get_calories_remained())

cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment='кофе'))
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
cash_calculator.add_record(Record(amount=3000, comment='бар в Танин др'))
print(cash_calculator.get_today_cash_remained('rub'))
