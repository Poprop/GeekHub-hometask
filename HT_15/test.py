# import fake_useragent
# import requests
# import csv
# from fake_useragent import UserAgent
# from pprint import pprint
# from bs4 import BeautifulSoup
# import time
#
# csv_name = "domains2.csv"
# target_url = "https://member.expireddomains.net/domains/combinedexpired/"
# user_agent = fake_useragent.UserAgent().random
#
#
# def login():
#     login_data = {
#         "login": "Poprop",
#         "password": f"655959Qq"
#     }
#     login_url = "https://www.expireddomains.net/login/"
#     with requests.Session() as session:
#         logining = session.post(login_url, data=login_data)
#         if 'Welcome' in logining.text:
#             print('Успішний вхід!')
#             target_response = session.get(target_url)
#             print(target_response.status_code)
#             print(target_response.text)
#
#
# def get_data(url):
#     headers = {"User-Agent": user_agent}
#     response = requests.get(url, headers=headers)
#     print(response.status_code)
#     print(response.text)
#     return response.content
#
#
# def make_csv(data):
#     headers = ["domain", "prices"]
#     with open(csv_name, "a+", encoding="utf-8", newline="") as csv_file:
#         writer = csv.DictWriter(csv_file, fieldnames=headers)
#         if csv_file.tell() == 0:
#             writer.writeheader()
#         writer.writerow(data)
#
#
# def get_info():
#     start = 0
#     while True:
#         url = f"https://www.expireddomains.net/expired-domains/?start={start}"
#         content = get_data(url)
#         soup = BeautifulSoup(content, features="html.parser")
#         domains = soup.find_all("td", class_="field_domain")
#         prices = soup.find_all("td", class_="field_price")
#         print(domains)
#         print(prices)
#
#         for domain, price in zip(domains, prices):
#             make_csv({"domain": domain.text, "prices": price.text})
#
#         next_page = soup.find("a", class_="next")
#         if not next_page:
#             print("That's all")
#             break
#
#         start += 25  # Incrementing start for the next page
#         time.sleep(20)
#
#
# if __name__ == "__main__":
#     login()
#     get_info()

# from bs4 import BeautifulSoup
# import requests
# from lxml import html
#
# url = "https://chromewebstore.google.com/detail/cosmos-price-in-usd-by-bi/kdiljojjjfdlnkagecglobmecndgifda"
#
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# name=soup.select_one('h1.Pa2dE').text,
# info=soup.select_one('div.uORbKe').text,
# print(name,info)


from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

url = "https://chromewebstore.google.com/detail/themebetacom/njifomhkhhoomffjgodaobmlcbdbefbe?hl=es"


# Парсимо HTML
soup = BeautifulSoup(url, 'html.parser')

# Отримуємо значення атрибутів з метатегів
og_url = soup.find("meta", property="og:url")["content"]
og_title = soup.find("meta", property="og:title")["content"]
og_description = soup.find("meta", property="og:description")["content"]

# Видобуваємо id з URL
id_ = urlparse(og_url).path.split('/').pop()

# Створюємо словник з отриманими даними
data = {
    'id': id_,
    'name': og_title,
    'description': og_description
}

print(data)