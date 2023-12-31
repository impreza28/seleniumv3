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


class Test():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_country_sort_check(self):
        self.driver.get(
            "http://localhost/litecart/public_html/admin/")
        self.driver.set_window_size(1236, 950)
        self.driver.find_element(By.NAME, "username").send_keys("admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin")
        self.driver.find_element(By.NAME, "login").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Countries')]").click()

        count_row = len(self.driver.find_elements(By.XPATH, "//*[@id='content']//table//tr[@class='row']"))

        # проверить, что страны в отсортированном порядке
        list_countries = []
        for i in range(count_row):
            countrie = self.driver.find_element(By.XPATH, f"//table/tbody/tr[{i + 2}]/td[5]").get_attribute(
                "textContent")
            list_countries.append(countrie)

            # zone = self.driver.find_element(By.XPATH, f"//table/tbody/tr[{i+2}]/td[6]").get_attribute("textContent")

        assert list_countries == sorted(list_countries), "Список стран на UI не отсортирован"

        # проверить зоны на сортировку
        for i in range(count_row):
            zone = self.driver.find_element(By.XPATH, f"//table/tbody/tr[{i + 2}]/td[6]").get_attribute("textContent")
            # если найдены зоны
            if zone != '0':
                # перейти в страну с зонами
                self.driver.find_element(By.XPATH, f"//table/tbody/tr[{i + 2}]/td[5]/a").click()

                zone_count = ((len(self.driver.find_elements(By.XPATH,
                                                          f"//table[@id='table-zones']/tbody/tr")))-2)
                #записать все зоны в лист
                list_zones=[]
                for j in range(zone_count):
                    countrie_zone = self.driver.find_element(By.XPATH,
                                                             f"//table[@id='table-zones']/tbody/tr[{j+2}]/td[3]").get_attribute("textContent")
                    list_zones.append(countrie_zone)

                #проверить зоны на сортировку
                assert list_zones == sorted(list_zones), "Список зон на UI не отсортирован"

                #вернуться к списку стран
                self.driver.find_element(By.NAME, "cancel").click()


    def login(self, email, password):
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.NAME, "login").click()

    def logout(self):
        self.driver.find_element(By.XPATH, "//a[@href='http://localhost/litecart/public_html/en/logout']").click()


def clear(s):
    return re.sub("[() - : .]", "", s)
