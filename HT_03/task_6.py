# Write a script to get the maximum and minimum value in a dictionary.
x = {
    'id': 17,
    'name': 'NoName',
    'freeze': -35,
    'count': 1,
    'admin': False,
    'errors': [400, 403],
    'email': None,
    'salary': 3750,
    'speed': 75.8,
    'file': 100644,
}


def only_nums(collection):
    if isinstance(collection, (int, float)):
        return collection
    elif isinstance(collection, list):
        return collection[0] if len(collection) > 0 and isinstance(collection[0], (int, float)) else 0
    else:
        return 0


maximal = (max(x.values(), key=only_nums))
minimal = (min(x.values(), key=only_nums))
print(maximal, minimal, sep="\n")

# import requests

# ------------------далі понесло і після пояснення ментора Євгенія про те що
# "Ще не вистачало щоб ви юзера просили словник вводити"   - я подумав а нащо юзеру вводити , якщо є апі які можуть
# постійно генерувати нам словники вирішив трохи повторити бібліотеку реквестс і реалізація данного інструментарію
# отримала реально цікаве використання p.s взагалі не Pro в данній бібліотеці ,витратив багато часу на гугління , але це
# був цікавий експіріенс-------------------------------------------------

# url = "https://api.exchangerate-api.com/v4/latest/UAH"
#
# currency_codes = ["USD", "RUB", "PLN", "EUR", "RUB"]
# currency_dict = {}
# response = requests.get(url)
# data = response.json()
# rates = data["rates"]
# for code in currency_codes:
#     if code in rates:
#         print(f"Курс UAH до {code} дорівнює {round(1 / rates[code], 2)}")
#         currency_dict[code] = round(1 / rates[code], 2)
#     else:
#         print(f"Курс {code} до UAH не доступний в API.")
# print(max(currency_dict.values()), min(currency_dict.values()), sep="\n")
