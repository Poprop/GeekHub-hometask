import requests
from requests import request
from pprint import pprint



def currently_exchange_rate(target_currency="UAH", base_currency="USD"):
    api_key = "4d7a8570a23a88492b3b56dba4d34a65"
    base_url = "http://api.exchangerate.host/"
    endpoint = "live"
    currencies = base_currency
    source = target_currency
    response = requests.get(
        f"{base_url}{endpoint}?access_key={api_key}&currencies={currencies}&source={source}")
    # print(f"{base_url}{endpoint}?access_key={api_key}&currencies={currencies}")

    if response.status_code == 200:
        data = response.json()
        result=list(data["quotes"].values())[0]
        return f"Current rate between {currencies} and {source} is {result}"


print(currently_exchange_rate())
