from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class CatalogPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def item(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#box-most-popular .product:nth-child(1) .image")

    def wait_add_item_in_cart(self, index):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".quantity"), f"{index + 1}"))

    def open(self):
        self.driver.get("http://localhost/litecart/public_html/en/")
        self.driver.maximize_window()

    def open_item(self):
        self.item.click()

