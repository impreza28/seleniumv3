
from selenium import webdriver
from selenium.webdriver.common.by import By
import re


class Test:
    def setup_method(self):

        self.chrome_driver = webdriver.Chrome()
        self.firefox_driver = webdriver.Firefox()
        self.vars = {}


    def teardown_method(self):
        self.firefox_driver.quit()
        self.chrome_driver.quit()


    def test_check_item_in_chrome(self):
        #открыть главную страницу
        self.open_home_page(self.chrome_driver)

        # получить название, полную цену и скидочную цену товара на главной странице
        item_name_home_page = self.get_item_name_home_page(self.chrome_driver)
        item_full_price_home_page = self.get_item_full_price_home_page(self.chrome_driver)
        item_discount_price_home_page = self.get_item_discount_price_home_page(self.chrome_driver)

        # получение и проверка стилей товара на главной странице

        # шрифт полной цены на главной странице
        item_full_price_line_through_home_page = self.get_item_full_price_line_through_home_page(self.chrome_driver)
        assert 'line-through' in item_full_price_line_through_home_page

        # цвет полной цены
        item_full_price_color_home_page = self.get_item_full_price_color_home_page(self.chrome_driver)
        assert '119, 119, 119' in item_full_price_color_home_page

        # цвет скидочной цены на главной странице
        item_discount_price_color_home_page = self.get_item_discount_price_color_home_page(self.chrome_driver)
        assert '204, 0, 0' in item_discount_price_color_home_page



        # шрифт скидочной цены на главной странице
        item_font_discount_price_home_page = self.get_item_font_discount_price_home_page(self.chrome_driver)
        assert item_font_discount_price_home_page == '700'

        # размер шрифта полной цены на главной странице
        item_font_size_price_home_page = self.get_item_font_size_price_home_page(self.chrome_driver)
        assert item_font_size_price_home_page == '14.4px'

        # размер шрифта скидочной цены на главной странице
        item_font_size_discount_price_home_page = self.get_item_font_size_discount_price_home_page(self.chrome_driver)
        assert item_font_size_discount_price_home_page == '18px'

        # нажать на карточку товара
        self.click_item(self.chrome_driver)


        # получить данные с карточки товара
        # название
        item_name = self.get_item_name(self.chrome_driver)
        # полная цена
        item_full_price = self.get_item_full_price(self.chrome_driver)
        # цена со скидкой
        item_discount_price = self.item_discount_price(self.chrome_driver)

        # проверить соответствие названия, полной и скидочной цены
        assert item_name_home_page == item_name, "Названия не совпадает"
        assert item_full_price_home_page == item_full_price, "Полная цена не совпадает"
        assert item_discount_price_home_page == item_discount_price, "Скидочная цена не совпадает"


        # проверить стили на карточке товара

        # шрифт полной цены
        item_full_price_line_through = self.get_item_full_price_line_through(self.chrome_driver)
        assert item_full_price_line_through == 'line-through solid rgb(102, 102, 102)'

        # цвет полной цены
        item_full_price_color = self.get_item_full_price_color(self.chrome_driver)
        assert item_full_price_color == 'rgba(102, 102, 102, 1)'

        # цвет скидочной цены
        item_discount_price_color = self.get_item_discount_price_color(self.chrome_driver)
        assert item_discount_price_color == 'rgba(204, 0, 0, 1)'

        # шрифт скидочной цены
        item_font_discount_price = self.get_item_font_discount_price(self.chrome_driver)
        assert item_font_discount_price == '700'

        # размер шрифта полной цены
        item_font_size_price = self.get_item_font_size_price(self.chrome_driver)
        assert item_font_size_price == '16px'

        # размер шрифта скидочной цены
        item_font_size_price = self.get_item_discount_size_price (self.chrome_driver)
        assert item_font_size_price == '22px'

    def test_check_item_in_firefox(self):
        #открыть главную страницу
        self.open_home_page(self.firefox_driver)

        # получить название, полную цену и скидочную цену товара на главной странице
        item_name_home_page = self.get_item_name_home_page(self.firefox_driver)
        item_full_price_home_page = self.get_item_full_price_home_page(self.firefox_driver)
        item_discount_price_home_page = self.get_item_discount_price_home_page(self.firefox_driver)

        # получение и проверка стилей товара на главной странице

        # шрифт полной цены на главной странице
        item_full_price_line_through_home_page = self.get_item_full_price_line_through_home_page(self.firefox_driver)
        assert 'line-through' in item_full_price_line_through_home_page

        # цвет полной цены
        item_full_price_color_home_page = self.get_item_full_price_color_home_page(self.firefox_driver)
        assert '119, 119, 119' in item_full_price_color_home_page

        # цвет скидочной цены на главной странице
        item_discount_price_color_home_page = self.get_item_discount_price_color_home_page(self.firefox_driver)
        assert '204, 0, 0' in item_discount_price_color_home_page



        # шрифт скидочной цены на главной странице
        item_font_discount_price_home_page = self.get_item_font_discount_price_home_page(self.firefox_driver)
        assert item_font_discount_price_home_page == '900'

        # размер шрифта полной цены на главной странице
        item_font_size_price_home_page = self.get_item_font_size_price_home_page(self.firefox_driver)
        assert item_font_size_price_home_page == '14.4px'

        # размер шрифта скидочной цены на главной странице
        item_font_size_discount_price_home_page = self.get_item_font_size_discount_price_home_page(self.firefox_driver)
        assert item_font_size_discount_price_home_page == '18px'

        # нажать на карточку товара
        self.click_item(self.firefox_driver)


        # получить данные с карточки товара
        # название
        item_name = self.get_item_name(self.firefox_driver)
        # полная цена
        item_full_price = self.get_item_full_price(self.firefox_driver)
        # цена со скидкой
        item_discount_price = self.item_discount_price(self.firefox_driver)

        # проверить соответствие названия, полной и скидочной цены
        assert item_name_home_page == item_name, "Названия не совпадает"
        assert item_full_price_home_page == item_full_price, "Полная цена не совпадает"
        assert item_discount_price_home_page == item_discount_price, "Скидочная цена не совпадает"


        # проверить стили на карточке товара

        # шрифт полной цены
        item_full_price_line_through = self.get_item_full_price_line_through(self.firefox_driver)
        assert item_full_price_line_through == 'line-through rgb(102, 102, 102)'

        # цвет полной цены
        item_full_price_color = self.get_item_full_price_color(self.firefox_driver)
        assert item_full_price_color == 'rgb(102, 102, 102)'

        # цвет скидочной цены
        item_discount_price_color = self.get_item_discount_price_color(self.firefox_driver)
        assert item_discount_price_color == 'rgb(204, 0, 0)'

        # шрифт скидочной цены
        item_font_discount_price = self.get_item_font_discount_price(self.firefox_driver)
        assert item_font_discount_price == '700'

        # размер шрифта полной цены
        item_font_size_price = self.get_item_font_size_price(self.firefox_driver)
        assert item_font_size_price == '16px'

        # размер шрифта скидочной цены
        item_font_size_discount_price = self.get_item_discount_size_price (self.firefox_driver)
        assert item_font_size_discount_price == '22px'





    # размер шрифта скидочной цены с карточки товара
    def get_item_discount_size_price(self, driver):
        return driver.find_element(By.CSS_SELECTOR,".campaign-price").value_of_css_property("font-size")
    # размер шрифта полной цены с карточки товара
    def get_item_font_size_price(self, driver):
        return driver.find_element(By.CSS_SELECTOR,".regular-price").value_of_css_property("font-size")

    # шрифт скидочной цены с карточки товара
    def get_item_font_discount_price(self, driver):
        return driver.find_element(By.CSS_SELECTOR,".campaign-price").value_of_css_property("font-weight")
    # цвет скидочной цены с карточки товара
    def get_item_discount_price_color(self, driver):
        return driver.find_element(By.CSS_SELECTOR,".campaign-price").value_of_css_property("color")

    # цвет полной цены с карточки товара
    def get_item_full_price_color(self, driver):
        return driver.find_element(By.CSS_SELECTOR,".regular-price").value_of_css_property("color")

    # шрифт полной цены с карточки товара
    def get_item_full_price_line_through(self, driver):
        return driver.find_element(By.CSS_SELECTOR,".regular-price").value_of_css_property("text-decoration")

    # получить название с карточки товара
    def get_item_name(self, driver):
        return driver.find_element(By.XPATH, "//h1[@class='title']").get_attribute("textContent")

    # получить полная цена с карточки товара
    def get_item_full_price(self,driver):
        return driver.find_element(By.XPATH, "//s[@class='regular-price']").get_attribute("textContent")

    # получить цена со скидкой с карточки товара
    def item_discount_price(self, driver):
        return driver.find_element(By.XPATH, "//strong[@class='campaign-price']").get_attribute("textContent")
    def click_item(self, driver):
        driver.find_element(By.XPATH, "//div[@id='box-campaigns']//a[@class='link']").click()

        # размер шрифта скидочной цены на главной странице
    def get_item_font_size_discount_price_home_page(self, driver):
        return driver.find_element(By.CSS_SELECTOR, ".campaign-price").value_of_css_property("font-size")

        # размер шрифта полной цены на главной странице
    def get_item_font_size_price_home_page(self, driver):
         return driver.find_element(By.CSS_SELECTOR, ".regular-price").value_of_css_property("font-size")

    # шрифт скидочной цены
    def get_item_font_discount_price_home_page(self, driver):
        return driver.find_element(By.CSS_SELECTOR, ".campaign-price").value_of_css_property("font-weight")

    # цвет скидочной цены на главной странице
    def get_item_discount_price_color_home_page(self,driver):
        return driver.find_element(By.CSS_SELECTOR, ".campaign-price").value_of_css_property("color")
    # цвет полной цены на главной странице
    def get_item_full_price_color_home_page(self, driver):
        return driver.find_element(By.CSS_SELECTOR, ".regular-price").value_of_css_property("color")

    # шрифт полной цены на главной странице
    def get_item_full_price_line_through_home_page(self, driver):
        return driver.find_element(By.CSS_SELECTOR, ".regular-price").value_of_css_property("text-decoration")


    # название товара на главной странице
    def get_item_name_home_page(self, driver):
        return driver.find_element(By.XPATH, "//div[@id='box-campaigns']//a[@class='link']").get_attribute("title")

    # полная цена главной страницы
    def get_item_full_price_home_page(self, driver):
        return driver.find_element(By.XPATH, "//div[@id='box-campaigns']//a[@class='link']//s["
                                                                  "@class='regular-price']").get_attribute("textContent")
    def get_item_discount_price_home_page(self, driver):
        return driver.find_element(By.XPATH, "//div[@id='box-campaigns']//a[@class='link']//strong["
                                                             "@class='campaign-price']").get_attribute("textContent")
    def open_home_page(self,driver):
        driver.get("http://localhost/litecart/public_html/en/")
        driver.set_window_size(1236, 950)





    def login(self, email, password):
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.NAME, "login").click()

    def login_admin_panel(self):
        self.driver.find_element(By.NAME, "username").send_keys('admin')
        self.driver.find_element(By.NAME, "password").send_keys('admin')
        self.driver.find_element(By.NAME, "login").click()

    def logout(self):
        self.driver.find_element(By.XPATH, "//a[@href='http://localhost/litecart/public_html/en/logout']").click()


def clear(s):
    return re.sub("[() - : .]", "", s)
