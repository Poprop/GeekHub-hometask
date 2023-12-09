import csv
import requests
import re
import time
import json


def sears_parser(product_url: str) -> csv:
    start_index = 1
    end_index = 48
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
    while True:
        url = (
            f"https://www.sears.com/api/sal/v3/products/search?startIndex={start_index}&endIndex={end_index}&searchType=category&catalogId=12605&"
            f"store=Sears&storeId=10153&zipCode=10101&bratRedirectInd=true&catPredictionInd=true&disableBundleInd=true&filterValueLimit=500&"
            f"includeFiltersInd=true&shipOrDelivery=true&solrxcatRedirection=true&sortBy=ORIGINAL_SORT_ORDER&whiteList"
            f"CacheLoad=false&eagerCacheLoad=true&slimResponseInd=true&catGroupId={group_id}&seoURLPath={url_slice}")

        with open(f"scv_file_{group_id}.csv", "a", newline="", encoding="utf-8") as csv_file:
            header = ["Item name", "Brand name", "Price", "Raiting", "Category"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=header)

            response = requests.get(url, headers=headers)
            print(response.status_code)
            if response.status_code == 200:
                try:
                    data = response.json()
                    items = data.get("items")

                    if not items:
                        break

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

                    start_index += len(items)
                    end_index += len(items)
                    time.sleep(2)
                except json.decoder.JSONDecodeError:
                    print("Помилка декодування JSON. Отриманий JSON пустий або щось інше.")
                    break
            else:
                print("Щось пішло не так " ,response.status_code)
                break

url = input("Ctrl+C and Ctrl + V : ")

print(sears_parser(url))
