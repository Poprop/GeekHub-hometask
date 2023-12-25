# import csv
# import json
# import requests
# from pprint import pprint
#
# start_index = 1
# end_index = 48
# products = []
# base_url = "https://www.sears.com"
# url = f"https://www.sears.com/api/ias/recommendation/product?item_category=Tools&item_category2=Tool%20Storage&type=top&limit=10&startIndex={start_index}&endIndex={end_index}&searchType=keyword&bratRedirectInd=true&catPredictionInd=true&filterValueLimit=500&includeFiltersInd=true&shipOrDelivery=true&solrxcatRedirection=true&sortBy=ORIGINAL_SORT_ORDER&whiteListCacheLoad=false&eagerCacheLoad=true&slimResponseInd=true&catRecommendationInd=true&zipcode=10101&catalogId=12605&store=Sears&storeId=10153"
# headers = {
#     'Accept': 'application/json, text/plain, */*',
#     'Accept-Encoding': '*',
#     'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
#     'Connection': 'keep-alive',
#     'Host': 'www.sears.com',
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
#     'X-Requested-With': 'XMLHttpRequest',
#     "Authorization": "SEARS",
# }
#
# response = requests.get(url, headers=headers)
# data = response.json()
#
# schemes = data.get("schemes", [])
# with open("scv_file", "w", newline="", encoding="utf-8") as csv_file:
#     csv_writer = csv.writer(csv_file)
#
#     header = ["Item name", "Price", "Item url", "Raiting", ]
#     csv_writer.writerow(header)
#
#     for scheme in schemes:
#         explanation = scheme.get("explanation", "")
#         items = scheme.get("items", [])
#         pprint(f"{explanation} {items}")
#
#         for item in items:
#             brand_name = items.get("brandName",'')
#             price = items.get("price",'')
#             item_url = base_url + items.get("url", "")
#             rating = items.get("rating",'')
#             csv_writer.writerow([brand_name, price, item_url, rating])
import csv
import json
import requests
from pprint import pprint


class SearsParser:
    def __init__(self, category_code="10153", start_index=1, end_index=48):
        self.start_index = start_index
        self.end_index = end_index
        self.category_code = category_code
        self.products = []
        self.base_url = "https://www.sears.com"

    def url_parser(self):

        url = f"https://www.sears.com/api/ias/recommendation/product?item_category=Tools&item_category2=Tool%20Storage&type=top&limit=10&startIndex={self.start_index}&endIndex={self.end_index}&searchType=keyword&bratRedirectInd=true&catPredictionInd=true&filterValueLimit=500&includeFiltersInd=true&shipOrDelivery=true&solrxcatRedirection=true&sortBy=ORIGINAL_SORT_ORDER&whiteListCacheLoad=false&eagerCacheLoad=true&slimResponseInd=true&catRecommendationInd=true&zipcode=10101&catalogId=12605&store=Sears&storeId=10153"
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': '*',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'www.sears.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            "Authorization": "SEARS",
        }
        response = requests.get(url, headers=headers)
        print(response.status_code)
        data = response.json()

        schemes = data.get("schemes", [])
        with open(f"scv_file_{self.category_code}.csv", "a", newline="", encoding="utf-8") as csv_file:
            header = ["Item name", "Price", "Item url", "Raiting", ]
            csv_writer = csv.DictWriter(csv_file, fieldnames=header)
            csv_writer.writeheader()
            try:
                for scheme in schemes:
                    explanation = scheme.get("explanation", "")
                    items = scheme.get("items", [])
                    pprint(f"{explanation} {items}")

                    for item in items:
                        brand_name = item.get("brandName", '')
                        price = item.get("price", '')
                        item_url = self.base_url + item.get("url", "")
                        rating = item.get("rating", '')
                        csv_writer.writerow({"Item name": brand_name,
                                             "Price": price,
                                             "Item url": item_url,
                                             "Raiting": rating})
            except Exception as e:
                print(f"{e} Error")


if __name__ == "__main__":
    parser = SearsParser(category_code="12605")
    print(parser.url_parser())
