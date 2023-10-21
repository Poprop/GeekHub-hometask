# Write a script to get the maximum and minimum value in a dictionary.
x = {"usd": 36, "eur": 40, "pln": 8.62, "gbp": 45.02, "chf": 40.7}
maximal = (max(x.values()))
minimal = (min(x.values()))
print(maximal, minimal, sep="\n")

import requests

# ------------------далі понесло і після пояснення ментора Євгенія про те що
# "Ще не вистачало щоб ви юзера просили словник вводити"   - я подумав а нащо юзеру вводити , якщо є апі які можуть
# постійно генерувати нам словники вирішив трохи повторити бібліотеку реквестс і реалізація данного інструментарію
# отримала реально цікаве використання p.s взагалі не Pro в данній бібліотеці ,витратив багато часу на гугління , але це
# був цікавий експіріенс-------------------------------------------------

url = "https://api.exchangerate-api.com/v4/latest/UAH"

currency_codes = ["USD", "RUB", "PLN", "EUR", "RUB"]
currency_dict = {}
response = requests.get(url)
data = response.json()
rates = data["rates"]
for code in currency_codes:
    if code in rates:
        print(f"Курс UAH до {code} дорівнює {round(1 / rates[code], 2)}")
        currency_dict[code] = round(1 / rates[code], 2)
    else:
        print(f"Курс {code} до UAH не доступний в API.")
print(max(currency_dict.values()), min(currency_dict.values()), sep="\n")
