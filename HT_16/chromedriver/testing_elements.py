# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from fake_useragent import UserAgent
# import time
# from datetime import datetime
# from PIL import Image
# from io import BytesIO
# import os
# import shutil
#
# user_agent_list = ["hello", "world", "geek_hub"]
# useragent = UserAgent()
#
# options = webdriver.ChromeOptions()
# options.add_argument(f"user-agent={useragent.random}")
# url = "https://robotsparebinindustries.com/"
# driver = webdriver.Chrome(options=options)
# output_folder_path = r"D:\Python study\GeekHub hometask\HT_16\output"
# if os.path.exists(output_folder_path):
#     os.rmdir(output_folder_path)
#     os.makedirs(output_folder_path)
#     print(f"Папку '{output_folder_path}' перезаписано.")
# else:
#     os.makedirs(output_folder_path)
#     print(f"Створено нову папку '{output_folder_path}'.")
#
# try:
#     # Відвідуємо сайт та натискаємо основну кнопку
#     driver.get(url=url)
#     order_button = driver.find_element(By.XPATH, "/html/body/div/header/div/ul/li[2]/a").click()
#
#     time.sleep(2)
#     print("Button is clicked")
#
#     # Натискання на додаткову кнопку, якщо вона є
#     try:
#         extra_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/button[2]")
#         extra_button.click()
#         time.sleep(5)
#         print("Extra button clicked")
#     except Exception as e:
#         print("Extra button not found:", e)
#
#     # Вибір частин робота (голова, тіло, ноги)
#     head_button = "/html/body/div/div/div[1]/div/div[1]/form/div[1]/select"
#     head_elements = {
#         1: "/html/body/div/div/div[1]/div/div[1]/form/div[1]/select/option[2]",
#         2: "/html/body/div/div/div[1]/div/div[1]/form/div[1]/select/option[3]",
#         3: "/html/body/div/div/div[1]/div/div[1]/form/div[1]/select/option[4]",
#         4: "/html/body/div/div/div[1]/div/div[1]/form/div[1]/select/option[5]",
#         5: "/html/body/div/div/div[1]/div/div[1]/form/div[1]/select/option[6]",
#         6: "/html/body/div/div/div[1]/div/div[1]/form/div[1]/select/option[7]"
#     }
#
#     # Вибір голови
#     head_select = driver.find_element(By.XPATH, head_button)
#     head_select.click()
#     head_option = driver.find_element(By.XPATH, head_elements[4])
#     head_option.click()
#     time.sleep(2)
#     body_button = driver.find_element(By.ID, "id-body-4").click()
#     time.sleep(2)
#     legs_element = "5"
#     legs_input = driver.find_element(By.CSS_SELECTOR, '.form-control[type="number"][min="1"][max="6"]')
#
#
#     driver.execute_script("arguments[0].scrollIntoView(true);", legs_input)
#     # driver.execute_script("window.scrollTo(0, arguments[0].offsetTop);", legs_input)
#
#     legs_input.send_keys(legs_element)
#
#     ship_address = "address sumgaitska100"
#     ship_input = driver.find_element(By.ID, "address")
#     ship_input.clear()
#     ship_input.send_keys(ship_address)
#     time.sleep(2)
#
#     preview_button = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div[1]/form/button[2]")
#     driver.execute_script("arguments[0].scrollIntoView(true);", preview_button)
#     time.sleep(2)
#     preview_button.click()
#     time.sleep(8)
#
#     receipt_el = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div[1]/div/div/p[1]")
#     receipt_number = receipt_el.text
#     print(f"receipt number is {receipt_number}")
#
#
#     dir = f"D:\Python study\GeekHub hometask\HT_16\output\screen_{receipt_number}.png"
#     photo_save = driver.find_element(By.ID, "robot-preview-image")
#     photo = driver.get_screenshot_as_png()
#
#     location = photo_save.location
#     size = photo_save.size
#
#     photo = Image.open(BytesIO(photo))
#     photo = photo.crop((location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height']))
#
#     photo.save(dir)
#     time.sleep(10)
#
# finally:
#     print("Smth wrong")
#     time.sleep(5)
#     driver.close()
#     driver.quit()
#
#
# # <div class="alert alert-danger" role="alert">Submit Button Stuck Error</div>
# import requests
# import csv
# import pandas as pd
# CSV_URL="https://robotsparebinindustries.com/orders.csv"
# def get_order_items(url=CSV_URL):
#     df = pd.read_csv(url)
#     result_dict = df[['Head', 'Body', 'Legs', 'Address']].to_dict(orient='records')
#     print(result_dict)
#     return result_dict
# print(get_order_items())

import pandas as pd
import requests
import csv

CSV_URL = "https://robotsparebinindustries.com/orders.csv"


# def get_orders_data(CSV_URL):
#     request = requests.get(CSV_URL)
#     request.raise_for_status()
#     rows = csv.reader(request.text.splitlines()[1:])
#     print([])

# def get_order_items(url=CSV_URL):
#     try:
#         df = pd.read_csv(url)
#         print(df)
#         result_dict = df[['Head', 'Body', 'Legs', 'Address']].to_dict(orient='records')
#         print(result_dict)
#         return result_dict
#     except Exception as e:
#         print(f"Помилка: {e}")
#         return None
#
# print(get_order_items())
from io import StringIO
from pprint import pprint
"""Отримання вмісту CSV"""
CSV_URL = "https://robotsparebinindustries.com/orders.csv"
def get_order_items(url=CSV_URL) -> list:
    try:
        response = requests.get(CSV_URL)
        response.raise_for_status()
        csv_data = response.text
        csv_reader = csv.DictReader(StringIO(csv_data))
        rows = list(csv_reader)
        updated_rows = [{k.lower(): v for k, v in row.items() if k.lower() != 'order number'} for row in rows]

        return updated_rows
    except Exception as e:
        print(f"Помилка: {e}")

"""Виклик екземпляру класу з вхідними данними"""
robot_data = get_order_items(CSV_URL)
pprint(robot_data)
