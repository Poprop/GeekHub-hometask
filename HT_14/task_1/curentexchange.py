import requests
from requests import request
from pprint import pprint


def exchangeRate(target_currency="UAH", base_currency="USD"):
    response = requests.get("https://open.er-api.com/v6/latest")

    if response.status_code == 200:
        data = response.json()
        exchange_rate = data["rates"].get(target_currency)
        time=data["time_last_update_utc"]
        if exchange_rate is not None:
           return f"The ratio of the {target_currency} to {base_currency} is {exchange_rate} for {time}"

