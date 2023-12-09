import fake_useragent
import requests
import csv
from fake_useragent import UserAgent
from pprint import pprint
from bs4 import BeautifulSoup
import time

url = "https://www.expireddomains.net/expired-domains/"
csv_name = "dommains2.csv"
target_url = "https://member.expireddomains.net/domains/combinedexpired/"
user=fake_useragent.UserAgent().random

def login():
    login_data = {
        "login": "Poprop",
        "password": f"655959Qq"
    }
    login_url = "https://www.expireddomains.net/login/"
    with requests.Session() as session:
        logining = session.post(login_url, data=login_data)
        if 'Welcome' in logining.text:
            print('Успішний вхід!')

            target_responce = session.get(target_url)
            print(target_responce.status_code)
            print(target_responce.text)


def get_data(url=url):
    login_data = {
        "login": "Poprop",
        "password": f"655959Qq"
    }
    login_url = "https://www.expireddomains.net/login/"
    headers = {"User-Agent": UserAgent().random}
    responce=requests.post(login_url,login_data,headers=headers)
    response = requests.get(url, headers)
    print(response.status_code)
    print(response.text)

    return response.content


def make_csv(data):
    headers = ["domain", "prices"]

    with open(csv_name, "a+", encoding="utf-8", newline="") as scv_file:
        writer = csv.DictWriter(scv_file, fieldnames=headers)
        if scv_file.tell() == 0:
            writer.writeheader()
        writer.writerow(data)


def get_info():
    while True:
        content = get_data(url)

        soup = BeautifulSoup(content, features="html.parser")
        domains = soup.find_all("td", class_="field_domain")
        prices = soup.find_all("td", class_="field_price")
        print(domains)
        print(prices)
        for domain, price in zip(domains, prices):
            make_csv({"domain": domain,
                      "prices": price})

        next_page = soup.find("a", class_="next")
        if not next_page:
            print("That`s all")
            break

        time.sleep(5)


print(get_info())
