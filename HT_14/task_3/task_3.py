""" http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної
 інформації про записи: цитата, автор, інфа про автора тощо.
- збирається інформація з 10 сторінок сайту.
- зберігати зібрані дані у CSV файл"""
import csv

import requests
from bs4 import BeautifulSoup
import pandas as pd


class Parser:
    def __init__(self, address):
        self.address = address
        self.author_text = ["text"]
        self.authors = ["author"]

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
                link_element = self.address + (span.find("a")["href"])
                bio_response = requests.get(link_element)
                bio_soup = BeautifulSoup(bio_response.content, "html.parser")

                name = bio_soup.find("h3", class_="author-title").text.strip()
                birthdate = bio_soup.find("span", class_="author-born-date").text.strip()
                born_location = bio_soup.find("span", class_="author-born-location").text.strip()
                description = bio_soup.find("div", class_="author-description").text.strip()
                df = pd.DataFrame({"Author bio": [
                    f'Name:{name},Birthday:{birthdate},Born Location:{born_location},Description:{description}']})
                df_existing = pd.read_csv("Authors&text.csv")
                df_existing = pd.concat([df_existing, df], ignore_index=True)
                df_existing.to_csv('Authors&text.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)
            return df_existing
        else:
            print(f"Unable to get page, status code: {response.status_code}")
            return pd.DataFrame

    def make_csv(self) -> None:
        with open("Authors&text.csv", "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(zip(self.author_text, self.authors))


if __name__ == "__main__":
    link = "http://quotes.toscrape.com/"
    parser = Parser(address=link)
    parser.author_text_parser()
    parser.author_info_parser()
    parser.make_csv()
    df_result = parser.about_author_info_parser()
    print(df_result)
