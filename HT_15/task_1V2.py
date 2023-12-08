# # import csv
# # import json
# # import requests
# # from pprint import pprint
# #
# # start_index = 1
# # end_index = 48
# # products = []
# # base_url = "https://www.sears.com"
# # url = f"https://www.sears.com/api/ias/recommendation/product?item_category=Tools&item_category2=Tool%20Storage&type=top&limit=10&startIndex={start_index}&endIndex={end_index}&searchType=keyword&bratRedirectInd=true&catPredictionInd=true&filterValueLimit=500&includeFiltersInd=true&shipOrDelivery=true&solrxcatRedirection=true&sortBy=ORIGINAL_SORT_ORDER&whiteListCacheLoad=false&eagerCacheLoad=true&slimResponseInd=true&catRecommendationInd=true&zipcode=10101&catalogId=12605&store=Sears&storeId=10153"
# # headers = {
# #     'Accept': 'application/json, text/plain, */*',
# #     'Accept-Encoding': '*',
# #     'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
# #     'Connection': 'keep-alive',
# #     'Host': 'www.sears.com',
# #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
# #     'X-Requested-With': 'XMLHttpRequest',
# #     "Authorization": "SEARS",
# # }
# #
# # response = requests.get(url, headers=headers)
# # data = response.json()
# #
# # schemes = data.get("schemes", [])
# # with open("scv_file", "w", newline="", encoding="utf-8") as csv_file:
# #     csv_writer = csv.writer(csv_file)
# #
# #     header = ["Item name", "Price", "Item url", "Raiting", ]
# #     csv_writer.writerow(header)
# #
# #     for scheme in schemes:
# #         explanation = scheme.get("explanation", "")
# #         items = scheme.get("items", [])
# #         pprint(f"{explanation} {items}")
# #
# #         for item in items:
# #             brand_name = items.get("brandName",'')
# #             price = items.get("price",'')
# #             item_url = base_url + items.get("url", "")
# #             rating = items.get("rating",'')
# #             csv_writer.writerow([brand_name, price, item_url, rating])
# import csv
# import json
# import requests
# from pprint import pprint
# import re
#
#
# def sears_parser(product_url: str) -> csv:
#     start_index = 1
#     end_index = 46
#     url_slice = product_url
#     base_url = "https://www.sears.com"
#
#     input_string = url_slice
#     pattern = r'\b(\d+)\b'
#
#     match = re.search(pattern, input_string)
#     if match:
#         cathegory_id = match.group(1)
#     url = (
#         f"https://www.sears.com/api/sal/v3/products/search?startIndex=1&endIndex=48&searchType=category&catalogId=12605&"
#         f"store=Sears&storeId=10153&zipCode=10101&bratRedirectInd=true&catPredictionInd=true&disableBundleInd=true&filterValueLimit=500&"
#         f"includeFiltersInd=true&shipOrDelivery=true&solrxcatRedirection=true&sortBy=ORIGINAL_SORT_ORDER&whiteList"
#         f"CacheLoad=false&eagerCacheLoad=true&slimResponseInd=true&catGroupId={cathegory_id}&seoURLPath={url_slice}")
#     headers = {
#         'Accept': 'application/json, text/plain, */*',
#         'Accept-Encoding': '*',
#         'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
#         'Connection': 'keep-alive',
#         'Host': 'www.sears.com',
#         'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
#         'X-Requested-With': 'XMLHttpRequest',
#         "Authorization": "SEARS",
#     }
#     response = requests.get(url, headers=headers)
#     data = response.json()
#
#     with open(f"scv_file_{cathegory_id}.csv", "w", newline="", encoding="utf-8") as csv_file:
#         header = ["Item name", "Brand name", "Price", "Raiting", "Category"]
#         csv_writer = csv.DictWriter(csv_file, fieldnames=header)
#         csv_writer.writeheader()
#
#         items = data.get("items")
#         for item in items:
#             name = item.get("name")
#             brand_name = item.get("brandName", '')
#             price = item.get("additionalAttributes", {}).get("salePrice", "")
#             rating = item.get("additionalAttributes", {}).get("rating", "")
#             category = item.get("category", "")
#             csv_writer.writerow({"Item name": name,
#                                  "Brand name": brand_name,
#                                  "Price": price,
#                                  "Raiting": rating,
#                                  "Category": category})
#
#
# # parser_id_request = input("Enter ID of item from interested cathegory")
#
# url = input("Ctrl+C and Ctrl + V ")
# print(sears_parser(url))
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
import re


def sears_parser(product_url: str) -> csv:
    start_index = 1
    end_index = 46
    url_income = product_url

    pattern_url_slice = r"https://www\.sears\.com/(.*?)/b-(\d+)"
    match = re.search(pattern_url_slice, url_income)
    if match:
        url_slice = match.group(1) + '/' + match.group(2)
        print(url_slice)

    pattern_group_id = r'/b-(\d+)\?'
    match = re.search(pattern_group_id, url_income)
    if match:
        group_id = match.group(1)
        print(group_id)
    url = (f"https://www.sears.com/api/sal/v3/products/search?startIndex=1&endIndex=48&searchType=category&catalogId=12605&"
       f"store=Sears&storeId=10153&zipCode=10101&bratRedirectInd=true&catPredictionInd=true&disableBundleInd=true&filterValueLimit=500&"
       f"includeFiltersInd=true&shipOrDelivery=true&solrxcatRedirection=true&sortBy=ORIGINAL_SORT_ORDER&whiteList"
       f"CacheLoad=false&eagerCacheLoad=true&slimResponseInd=true&catGroupId={group_id}&seoURLPath={url_slice}")
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


    with open(f"scv_file_{group_id}.csv", "w", newline="", encoding="utf-8") as csv_file:
        header = ["Item name", "Brand name", "Price", "Raiting", "Category"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=header)
        csv_writer.writeheader()

        items = data.get("items")
        for item in items:
            name = item.get("name")
            brand_name = item.get("brandName", '')
            price = item.get("additionalAttributes", {}).get("salePrice", "")
            rating = item.get("additionalAttributes", {}).get("rating", "")
            category = item.get("category", "")
            csv_writer.writerow({"Item name": name,
                                 "Brand name": brand_name,
                                 "Price": price,
                                 "Raiting": rating,
                                 "Category": category})

# url = input("Ctrl+C and Ctrl + V ")
url="https://www.sears.com/tools/b-1020000?adcell=hp_CatLink_Tools"
print(sears_parser(url))
