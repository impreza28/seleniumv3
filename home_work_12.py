# Generated by Selenium IDE
import pytest
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime
import re


class TestAddItem():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_add_item(self):
        self.driver.get(
            "http://localhost/litecart/public_html/admin/")
        self.driver.set_window_size(1036, 956)
        self.driver.find_element(By.NAME, "username").send_keys("admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin")
        self.driver.find_element(By.NAME, "login").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Catalog')]").click()
        self.driver.find_element(By.LINK_TEXT, "Add New Product").click()
        self.driver.find_element(By.NAME, "status").click()

        date_time = clear(str(datetime.datetime.now().time()))

        name_item = f"Жареная утка{date_time}"

        self.driver.find_element(By.NAME, "name[en]").send_keys(name_item)
        self.driver.find_element(By.NAME, "code").click()
        self.driver.find_element(By.NAME, "code").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) tr:nth-child(2) input").click()
        self.driver.find_element(By.NAME, "product_groups[]").click()

        file = os.path.abspath('img.png')
        self.driver.find_element(By.NAME, "new_images[]").send_keys(file)

        self.driver.find_element(By.NAME, "date_valid_from").send_keys("10-01-2023")
        self.driver.find_element(By.NAME, "date_valid_to").send_keys("10-01-2024")
        self.driver.find_element(By.LINK_TEXT, "Information").click()
        self.driver.find_element(By.NAME, "manufacturer_id").click()
        dropdown = self.driver.find_element(By.NAME, "manufacturer_id")
        dropdown.find_element(By.XPATH, "//option[. = 'ACME Corp.']").click()
        self.driver.find_element(By.NAME, "keywords").send_keys("утка")

        self.driver.find_element(By.NAME, "short_description[en]").send_keys("утька")
        self.driver.find_element(By.CSS_SELECTOR, ".trumbowyg-editor").send_keys('утька')

        self.driver.find_element(By.NAME, "head_title[en]").send_keys("утька")

        self.driver.find_element(By.NAME, "meta_description[en]").send_keys("утька")
        self.driver.find_element(By.LINK_TEXT, "Prices").click()
        self.driver.find_element(By.NAME, "purchase_price").send_keys("1000")
        self.driver.find_element(By.NAME, "save").click()
        self.driver.find_element(By.NAME, "query").send_keys(f"{name_item}")
        self.driver.find_element(By.NAME, "query").send_keys(Keys.ENTER)
        item = self.driver.find_element(By.XPATH, "//table[@class='dataTable']//tr[@class='row']/td[3]").get_attribute("textContent")


        assert item == f" {name_item}", "Имя товара не совпадает"


        #self.driver.find_elements()

    def login(self, email, password):
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.NAME, "login").click()
    def logout(self):
        self.driver.find_element(By.XPATH, "//a[@href='http://localhost/litecart/public_html/en/logout']").click()






def clear(s):
    return re.sub("[() - : .]", "", s)
