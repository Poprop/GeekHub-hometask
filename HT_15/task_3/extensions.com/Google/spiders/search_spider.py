import scrapy
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup


class SearchSpider(scrapy.Spider):
    name = "search_spider"
    start_urls = "https://chrome.google.com/webstore/sitemap"

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls, callback=self.parse)

    def parse(self, response):
        # responce = scrapy.Request(url=self.start_urls)
        soup = BeautifulSoup(response.body, "xml")

        for url in soup.select("sitemap > loc "):
            yield scrapy.Request(url=url.text, callback=self.url_parser)

    def url_parser(self, response):
        soup = BeautifulSoup(response.text, "xml")

        for url in soup.select("url > loc"):
            if "detail" not in url.text:
                print(url)
                continue
            yield scrapy.Request(url=url.text, callback=self.parse_chrome_apps)

    def parse_chrome_apps(self, response, **kwargs):

        id_ = response.css('[property="og:url"]::attr(content)').get().split('/').pop()
        yield {
            'id': f'{id_}',
            'name': response.css('[property="og:title"]::attr(content)').get(),
            'description': response.css('[property="og:description"]::attr(content)').get()
        }
