""" http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної
 інформації про записи: цитата, автор, інфа про автора тощо.
- збирається інформація з 10 сторінок сайту.
- зберігати зібрані дані у CSV файл"""
import csv

import requests
from bs4 import BeautifulSoup
import pandas as pd


class Parser:
    headers_created = False
    def __init__(self, address):
        self.address = address
        self.author_text = []
        self.authors = []
        self.author_bio_frame = []


    def author_text_parser(self) -> None:
        response = requests.get(self.address)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            text_info = soup.findAll("span", class_="text")
            self.author_text += [message.text for message in text_info]

    def author_info_parser(self) -> None:
        response = requests.get(self.address)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            author_info = soup.find_all('small', class_='author')
            self.authors += [author.text for author in author_info]

    def about_author_info_parser(self):
        response = requests.get(self.address)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            authors = soup.find_all('small', {'class': 'author'})

            for author in authors:
                span = author.parent
                bio_address = "https://quotes.toscrape.com/"
                link_element = bio_address + (span.find("a")["href"])
                bio_response = requests.get(link_element)
                bio_soup = BeautifulSoup(bio_response.content, "html.parser")

                name_element = bio_soup.find("h3", class_="author-title")
                name = name_element.text.strip() if name_element else "N/A"
                birthdate_element = bio_soup.find("span", class_="author-born-date")
                birthdate = birthdate_element.text.strip() if birthdate_element else "N/A"
                born_element = bio_soup.find("span", class_="author-born-location")
                born_location = born_element.text.strip() if born_element else "N/A"
                description_element = bio_soup.find("div", class_="author-description")
                description = description_element.text.strip() if description_element else "N/A"

                author_data = f'Name: {name}\nBirthday: {birthdate}\nBorn Location: {born_location}\nDescription: {description}'

                self.author_bio_frame.append(author_data)
        else:
            print(f"Unable to get page, status code: {response.status_code}")
            return pd.DataFrame()

    def make_csv(self) -> None:
        with open("Authors&text.csv", "a", newline="", encoding="utf-8") as csv_file:
            fields = ["Text", "Name", "Bio"]
            writer = csv.DictWriter(csv_file, fieldnames=fields)

            if not Parser.headers_created:
                writer.writeheader()
                Parser.headers_created = True

            for text, author, bio in zip(self.author_text, self.authors, self.author_bio_frame):
                writer.writerow({"Text": text,
                                 "Name": author,
                                 "Bio": bio})


if __name__ == "__main__":
    page_amount = int(input("enter amount of pages: "))
    for page_num in range(1, page_amount + 1):
        link = f"https://quotes.toscrape.com/page/{str(page_num)}/"
        parser = Parser(address=link)
        parser.author_text_parser()
        parser.author_info_parser()
        parser.about_author_info_parser()
        parser.make_csv()
