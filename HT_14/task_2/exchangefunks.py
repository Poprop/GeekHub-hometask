import requests
from pprint import pprint

"""https://api.exchangerate.host/live?access_key=4d7a8570a23a88492b3b56dba4d34a65"""


def currently_exchange_rate(income_currencies):
    api_key = "4d7a8570a23a88492b3b56dba4d34a65"
    base_url = "http://api.exchangerate.host/"
    endpoint = "live"
    currencies = ",".join(income_currencies)
    response = requests.get(
        f"{base_url}{endpoint}?access_key={api_key}&currencies={currencies}")
    # print(f"{base_url}{endpoint}?access_key={api_key}&currencies={currencies}")

    if response.status_code == 200:
        data = response.json()
        return data


"""https://api.exchangerate.host/historical?date=YYYY-MM-DD
http://api.exchangerate.host/historical&date=2023-11-11?access_key=4d7a8570a23a88492b3b56dba4d34a65&currencies=EUR,UAH"""


def history_of_exchange_rates(income_date, income_currencies):
    api_key = "?access_key=4d7a8570a23a88492b3b56dba4d34a65"
    base_url = "http://api.exchangerate.host/"
    endpoint = "historical"
    date = "&date=" + "-".join(income_date)
    currencies = ",".join(income_currencies)
    # currencies=income_currencies
    response = requests.get(f"{base_url}{endpoint}{date}{api_key}&currencies={currencies}")
    if response.status_code == 200:
        data = response.json()
        return data


# pprint(history_of_exchange_rates("2023", "11", "11","EUR,USD,UAH"))

def period_exchange_information(income_start, income_end, income_currencies):
    api_key = "?access_key=4d7a8570a23a88492b3b56dba4d34a65"
    base_url = "http://api.exchangerate.host/"
    endpoint = "timeframe"
    start_date = "-".join(income_start)
    end_date = "-".join(income_end)
    currencies = ",".join(income_currencies)

    response = requests.get(
        f"{base_url}{endpoint}{api_key}&currencies={currencies}&start_date={start_date}&end_date={end_date}")
    if response.status_code == 200:
        data = response.json()
        return data
