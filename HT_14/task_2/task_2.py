# Створіть програму для отримання курсу валют за певний період.
# - отримати від користувача дату (це може бути як один день так і інтервал - початкова і кінцева дати,
# продумайте механізм реалізації) і назву валюти
# - вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному інтервалі)
# - не забудьте перевірку на валідність введених даних

import requests
from pprint import pprint
import re
from HT_14.task_2.exchangefunks import currently_exchange_rate, history_of_exchange_rates, period_exchange_information

date_pattern = re.compile(r'^(?:19|20)\d\d,(?:0[1-9]|1[0-2]),(?:0[1-9]|[12][0-9]|3[01])$')


def exchanger():
    print("Choose necessary function of exchange manager you need:")
    menu_options = {"1": "currently_exchange_rate",
                    "2": "history_of_exchange_rates",
                    "3": "period_exchange_information",
                    "4": "exit"}
    for key, value in menu_options.items():
        print(f"{key} <-------- {value}")
    choice = input("Enter your choice using number: ")
    if choice in menu_options.keys():
        if choice == "1":
            currency = input("Enter currency you interested in by using international "
                             "format RUB,EUR,USD,UAH with coma separator: ").upper().split(",")
            result = currently_exchange_rate(currency)["quotes"]
            for curency, rate in result.items():
                print(f"{curency} ---- {rate}")
        if choice == "2":
            currency = input("Enter currency you interested in by using international "
                             "format RUB,EUR,USD,UAH with coma separator: ").upper().split(",")
            try:
                input_date = input("Enter start date in format YYYY,MM,DD: ")
                if date_pattern.match(input_date):
                    search_date = input_date.split(",")
            except ValueError:
                print("Invalid date format. Please enter in YYYY,MM,DD format.")
            result = history_of_exchange_rates(income_date=search_date, income_currencies=currency)
            date = result["date"]
            quote = result["quotes"].items()
            print(f"For {date} exchange rate was: ")
            for curency, rate in quote:
                print(f"{curency} ---- {rate}")
        if choice == "3":
            try:
                input_start = input("Enter start date in format YYYY,MM,DD: ")
                if date_pattern.match(input_start):
                    start_date = input_start.split(",")
            except ValueError:
                print("Invalid date format. Please enter in YYYY,MM,DD format.")
            try:
                input_end = input("Enter end date in format YYYY,MM,DD: ")
                if date_pattern.match(input_end):
                    end_date = input_end.split(",")
            except ValueError:
                print("Invalid date format. Please enter in YYYY,MM,DD format.")

            currency = input("Enter currency you interested in by using international "
                             "format RUB,EUR,USD,UAH with coma separator: ").upper().split(",")
            result = period_exchange_information(income_start=start_date, income_end=end_date,
                                                 income_currencies=currency)
            quote = result["quotes"].items()
            print(f"The exchange rate in period from {input_start} to {input_end} was:")
            for date, rate_dict in quote:
                for code, rate in rate_dict.items():
                    print(f"On {date} for {code} was {rate} rate")
        if choice == "4":
            return "Good bye"


print(exchanger())

