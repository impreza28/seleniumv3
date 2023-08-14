from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class ItemPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)



    @property
    def size_item(self):
        return self.driver.find_element(By.XPATH, "//option[2]")
    @property
    def button_size_item(self):
        return self.driver.find_element(By.NAME, "options[Size]")

    @property
    def button_add_to_cart(self):
        return self.driver.find_element(By.NAME, "add_cart_product")




# # # # # # # # #  # # #  # # #  # # #  # # #  # # #
    def select_size_item(self):
        self.size_item.click()

    def get_count_menu_size_in_item(self):
        return len(self.driver.find_elements(By.NAME, "options[Size]"))
    def click_button_size_item(self):
        self.button_size_item.click()
    def add_item_to_cart(self):
        self.button_add_to_cart.click()




