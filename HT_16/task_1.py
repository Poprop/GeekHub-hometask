import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from fake_useragent import UserAgent
from PIL import Image
import os
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from typing import Tuple
import requests
import csv
from io import StringIO


class Robot:

    def __init__(self, address: str, body: str, head: str, legs: str):
        self.head = head
        self.body = body
        self.legs = legs
        self.address = address

        self.user_agent_list = ["hello", "world", "geek_hub"]
        self.useragent = UserAgent()
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(f"user-agent={self.useragent.random}")
        self.url = "https://robotsparebinindustries.com/"
        self.driver = webdriver.Chrome(options=self.options)
        self.receipt = None
        self.WAIT_TIME = 5

    def site_initiation(self):
        try:
            self.driver.get(url=self.url)
            order_button = self.driver.find_element(By.XPATH, "/html/body/div/header/div/ul/li[2]/a").click()

            time.sleep(2)
            print("Button is cliked")
            try:
                extra_button = self.driver.find_element(By.XPATH,
                                                        "/html/body/div/div/div[2]/div/div/div/div/div/button[2]")
                extra_button.click()
                time.sleep(5)
                print("Extra button clicked")
            except Exception as e:
                print("Extra button not found:", e)

        except Exception as e:
            print(e)
        print("сайт відкрився")

    def dir_initiation(self):
        output_folder_path = r"D:\Python study\GeekHub hometask\HT_16\output"
        if os.path.exists(output_folder_path):
            os.removedirs(output_folder_path)
            os.makedirs(output_folder_path)
            print(f"Папку '{output_folder_path}' перезаписано.")
        else:
            os.makedirs(output_folder_path)
            print(f"Створено нову папку '{output_folder_path}'.")

        print("Папку створено")

    def wait_locator(self, locator: Tuple[str, str], is_click: bool = True):
        driver_wait = WebDriverWait(self.driver, self.WAIT_TIME)
        element = driver_wait.until(EC.presence_of_element_located(locator))
        if is_click:
            element.click()

    def head_choose(self):
        head_button = "/html/body/div/div/div[1]/div/div[1]/form/div[1]/select"
        head_elements = {"1": r"/html/body/div/div/div[1]/div/div[1]/form/div[1]/select/option[2]",
                         "2": r"/html/body/div/div/div[1]/div/div[1]/form/div[1]/select/option[3]",
                         "3": r"/html/body/div/div/div[1]/div/div[1]/form/div[1]/select/option[4]",
                         "4": r"/html/body/div/div/div[1]/div/div[1]/form/div[1]/select/option[5]",
                         "5": r"/html/body/div/div/div[1]/div/div[1]/form/div[1]/select/option[6]",
                         "6": r"/html/body/div/div/div[1]/div/div[1]/form/div[1]/select/option[7]"}
        head_select = self.driver.find_element(By.XPATH, head_button)
        head_select.click()
        head_option = self.driver.find_element(By.XPATH, head_elements[self.head])
        head_option.click()
        time.sleep(10)
        print("голову створено")

    def body_choose(self):
        try:
            body_button = self.driver.find_element(By.ID, f"id-body-{self.body}")
            body_button.click()
            time.sleep(10)
            print('тіло створено')
        except NoSuchElementException as e:
            if not (0 < int(self.body) <= 6):
                print("wrong value of body type")
            else:
                print(f"Element not found: {e}")

    def legs_and_ship_info(self):
        legs_element = self.legs
        legs_input = self.driver.find_element(By.CSS_SELECTOR, '.form-control[type="number"][min="1"][max="6"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", legs_input)
        time.sleep(4)
        legs_input.clear()
        legs_input.send_keys(legs_element)

        ship_address = self.address
        ship_input = self.driver.find_element(By.CSS_SELECTOR, "input#address")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ship_input)
        ship_input.clear()
        ship_input.send_keys(ship_address)
        print("дані доставки і ноги обрану")

    def process_order(self):
        while True:
            # Scroll to and click the order button
            order_button = self.driver.find_element(By.CSS_SELECTOR, "button#order.btn.btn-primary")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", order_button)
            time.sleep(10)
            order_button.click()

            # Check if the order was successful
            try:
                self.wait_locator((By.ID, 'receipt'), False)
                return True
            except (WebDriverException, NoSuchElementException, TimeoutException):
                # If not, check if there was an alert
                try:
                    self.driver.find_element(By.CLASS_NAME, 'alert-danger')
                    continue  # If alert is present, repeat the loop
                except (WebDriverException, NoSuchElementException):
                    return False  # If alert is not present, return False

    def save_receipt(self):

        receipt_el = self.driver.find_element(By.CSS_SELECTOR, "p.badge.badge-success")
        receipt_number = receipt_el.text
        print(f"receipt number is {receipt_number}")
        self.receipt = receipt_number
        return self.receipt
        print("Чек зберіг")

    def save_image(self):
        dir = f"D:\Python study\GeekHub hometask\HT_16\output\screen_{self.receipt}.png"
        # photo_save = self.driver.find_element(By.ID, "robot-preview-image")
        # photo = self.driver.get_screenshot_as_png()
        #
        # location = photo_save.location
        # size = photo_save.size
        #
        # photo = Image.open(BytesIO(photo))
        # photo = photo.crop(
        #     (location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height']))
        #
        # photo.save(dir)
        # time.sleep(10)
        # print("створено фото і збережено")
        head_img_url = self.driver.find_element(By.XPATH, '//img[@alt="Head"]').get_attribute('src')
        body_img_url = self.driver.find_element(By.XPATH, '//img[@alt="Body"]').get_attribute('src')
        legs_img_url = self.driver.find_element(By.XPATH, '//img[@alt="Legs"]').get_attribute('src')

        head_img = Image.open(requests.get(head_img_url, stream=True).raw)
        body_img = Image.open(requests.get(body_img_url, stream=True).raw)
        legs_img = Image.open(requests.get(legs_img_url, stream=True).raw)

        img_width = max(head_img.size[0], body_img.size[0], legs_img.size[0])
        img_height = head_img.size[1] + body_img.size[1] + legs_img.size[1]

        img = Image.new("RGBA", (img_width, img_height))
        img.paste(head_img, (int((img_width - head_img.size[0]) / 2), 0))
        img.paste(body_img, (int((img_width - body_img.size[0]) / 2), head_img.size[1]))
        img.paste(legs_img, (int((img_width - legs_img.size[0]) / 2), head_img.size[1] + body_img.size[1]))
        img.save(dir)

    def next_robot(self):
        try:
            another_robot_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "order-another"))
            )
            another_robot_button.click()
        except TimeoutException:
            print("Next Robot button not found within the expected time.")

    def process_robot(self):
        self.site_initiation()
        self.head_choose()
        self.body_choose()
        self.legs_and_ship_info()
        self.process_order()
        self.save_receipt()
        self.save_image()
        self.next_robot()

    def __del__(self):
        self.driver.quit()


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
for data in robot_data:
    robot = Robot(**data)
    robot.process_robot()
