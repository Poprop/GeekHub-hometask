import csv
import os
import time
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

DOMAINS_FILE = "domains.csv"
BASE_URL = "https://member.expireddomains.net/domains/combinedexpired/"
WAIT_TIME = 5





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
    while True:
        page_content = get_data(BASE_URL)

        soup = BeautifulSoup(page_content, features="html.parser")
        rows = soup.find_all("td", class_="field_domain")
        domain_text_list = [row.text for row in rows]

        write_to_csv(domain_text_list)

        next_page = soup.find("a", class_="next")
        if not next_page:
            print("Збір даних завершено!")
            break

        time.sleep(WAIT_TIME)


print(find_info())
