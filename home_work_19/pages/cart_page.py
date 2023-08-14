from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By



class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    @property
    def catr_lick(self):
        return self.driver.find_element(By.LINK_TEXT, "Checkout »")
    @property
    def shortcuts(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "ul.shortcuts > li")

    @property
    def first_shortcut(self):
        return self.driver.find_element(By.XPATH, "//ul[@class='shortcuts']/li/a")
    @property
    def title_item(self):
        return self.driver.find_element(By.XPATH, "//form[@name='cart_form']//strong")
    @property
    def button_remove_item(self):
        return self.driver.find_element(By.NAME, "remove_cart_item")
    @property
    def items_in_table(self):
        a=self.driver.find_elements(By.CSS_SELECTOR, "table.dataTable.rounded-corners td.item")
        return a



    def open_cart(self):
        self.catr_lick.click()
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.ID, "main-wrapper")))

    def get_count_items(self):
        a=self.shortcuts
        return len(a)
    def select_shortcut(self):
        self.first_shortcut.click()
        # ждать переключения на товар
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//ul[@class='shortcuts']/li[1]/a[@class='inact act']")))

    def get_title_item(self):
        return self.title_item.get_attribute("textContent")

    def wait_shrotcuts_invisible(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element_located((By.XPATH, "//ul[@class='shortcuts']")))

    def del_item(self, name_item):
        # удалить товар
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((By.NAME, "remove_cart_item")))
        self.button_remove_item.click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element_located((By.XPATH, f"//strong[contains(.,'{name_item}')]")))
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, f"//div[@id='checkout-cart-wrapper' and @style='opacity: 1;']")))

    def get_count_items_in_table(self):
        a= len(self.items_in_table)
        return a

    def get_title_item_in_table(self, index):
        return self.driver.find_element(By.XPATH, f"//table[@class='dataTable rounded-corners']//tr[{index}]/td[@class='item']").get_attribute("textContent")

    def wait_link_Back(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((By.LINK_TEXT, "<< Back")))