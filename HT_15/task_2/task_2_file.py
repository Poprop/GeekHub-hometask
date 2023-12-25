import fake_useragent
import requests
import csv
from fake_useragent import UserAgent
from pprint import pprint
from bs4 import BeautifulSoup
import time

url = "https://www.expireddomains.net/expired-domains/?start=25#listing"
csv_name = "dommains2.csv"
target_url = "https://member.expireddomains.net/domains/combinedexpired/"
user = fake_useragent.UserAgent().random




def get_data(url=url):
    headers = {"User-Agent": UserAgent().random}
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
    start = 25
    while True:
        content = get_data(f"https://www.expireddomains.net/expired-domains/?start={start}#listing")
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
        start += 25
        time.sleep(20)


print(get_info())
