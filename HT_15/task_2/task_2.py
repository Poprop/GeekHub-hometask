import csv
import os
import time
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

DOMAINS_FILE = "domains.csv"
WAIT_TIME = 20


def get_data(url, params=None, headers=None):
    if headers is None:
        headers = {"User-Agent": UserAgent().random}

    response = requests.get(url, params=params, headers=headers)
    return response.content


def write_to_csv(data):
    headers = ["Domain"]
    file_exists = os.path.exists(DOMAINS_FILE)

    with open(DOMAINS_FILE, "a+", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or file.tell() == 0:
            writer.writerow(headers)

        for row in data:
            writer.writerow([row])


def find_info():
    items_count = 25
    while True:

        page_content = get_data(f"https://www.expireddomains.net/expired-domains/?start={items_count}#listing")

        soup = BeautifulSoup(page_content, features="html.parser")
        rows = soup.find_all("td", class_="field_domain")
        print(rows)
        domain_text_list = [row.text for row in rows]

        write_to_csv(domain_text_list)
        print(f"I`m working ,already added {items_count} dommains")
        items_count += len(domain_text_list)
        time.sleep(WAIT_TIME)


print(find_info())
