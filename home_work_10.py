
from selenium import webdriver
from selenium.webdriver.common.by import By
import re


class Test:
    def setup_method(self):

        self.driver = webdriver.Chrome()

        self.firefox_driver = webdriver.Firefox()
        #self.driver= self.chrome_driver
        self.vars = {}


    def teardown_method(self):
        self.driver.quit()

    #@pytest.mark.parametrize("driver", [(webdriver.Firefox()), (webdriver.Chrome())])
    def test_item_check(self):
        self.driver.get("http://localhost/litecart/public_html/en/")
        self.driver.set_window_size(1236, 950)

        # получить данные о карточке с главной страницы
        # название
        item_name_home_page = self.driver.find_element(By.XPATH, "//div[@id='box-campaigns']//a[@class='link']").get_attribute("title")
        # полная цена
        item_full_price_home_page = self.driver.find_element(By.XPATH, "//div[@id='box-campaigns']//a[@class='link']//s["
                                                             "@class='regular-price']").get_attribute("textContent")
        # цена со скидкой
        item_discount_price_home_page = self.driver.find_element(By.XPATH, "//div[@id='box-campaigns']//a[@class='link']//strong["
                                                             "@class='campaign-price']").get_attribute("textContent")

        # проверка стилей товара на главной странице

        # шрифт полной цены на главной странице
        item_full_price_line_through_home_page = self.driver.find_element(By.CSS_SELECTOR, ".regular-price").value_of_css_property("text-decoration")
        #assert item_full_price_line_through_home_page == 'line-through solid rgb(119, 119, 119)'
        assert 'line-through' in item_full_price_line_through_home_page

        # цвет полной цены на главной странице
        item_full_price_color_home_page = self.driver.find_element(By.CSS_SELECTOR, ".regular-price").value_of_css_property("color")
        #assert item_full_price_color_home_page == 'rgba(119, 119, 119, 1)'
        assert '119, 119, 119' in item_full_price_color_home_page

        # цвет скидочной цены на главной странице
        item_discount_price_color_home_page = self.driver.find_element(By.CSS_SELECTOR, ".campaign-price").value_of_css_property("color")
        #assert item_discount_price_color_home_page == 'rgba(204, 0, 0, 1)'
        assert '204, 0, 0' in item_discount_price_color_home_page

        # шрифт скидочной цены на главной странице
        item_font_discount_price_home_page = self.driver.find_element(By.CSS_SELECTOR, ".campaign-price").value_of_css_property("font-weight")
        assert item_font_discount_price_home_page == '700'

        # размер шрифта полной цены на главной странице
        item_font_size_price_home_page = self.driver.find_element(By.CSS_SELECTOR, ".regular-price").value_of_css_property("font-size")
        assert item_font_size_price_home_page == '14.4px'

        # размер шрифта скидочной цены на главной странице
        item_font_size_price_home_page = self.driver.find_element(By.CSS_SELECTOR, ".campaign-price").value_of_css_property("font-size")
        assert item_font_size_price_home_page == '18px'

        # нажать на карточку товара
        self.driver.find_element(By.XPATH, "//div[@id='box-campaigns']//a[@class='link']").click()

        # получить данные с карточки товара
        # название
        item_name = self.driver.find_element(By.XPATH, "//h1[@class='title']").get_attribute("textContent")
        # полная цена
        item_full_price = self.driver.find_element(By.XPATH, "//s[@class='regular-price']").get_attribute("textContent")
        # цена со скидкой
        item_discount_price = self.driver.find_element(By.XPATH, "//strong[@class='campaign-price']").get_attribute("textContent")

        # проверить соответствие названия, полной и скидочной цены
        assert item_name_home_page == item_name, "Названия не совпадает"
        assert item_full_price_home_page == item_full_price, "Полная цена не совпадает"
        assert item_discount_price_home_page == item_discount_price, "Скидочная цена не совпадает"

        # проверить стили на карточке товара

        # шрифт полной цены
        item_full_price_line_through = self.driver.find_element(By.CSS_SELECTOR,
                                                                          ".regular-price").value_of_css_property(
            "text-decoration")
        assert item_full_price_line_through == 'line-through solid rgb(102, 102, 102)'

        # цвет полной цены
        item_full_price_color = self.driver.find_element(By.CSS_SELECTOR,
                                                                   ".regular-price").value_of_css_property("color")
        assert item_full_price_color == 'rgba(102, 102, 102, 1)'

        # цвет скидочной цены
        item_discount_price_color = self.driver.find_element(By.CSS_SELECTOR,
                                                                       ".campaign-price").value_of_css_property("color")
        assert item_discount_price_color == 'rgba(204, 0, 0, 1)'

        # шрифт скидочной цены
        item_font_discount_price = self.driver.find_element(By.CSS_SELECTOR,
                                                                      ".campaign-price").value_of_css_property(
            "font-weight")
        assert item_font_discount_price == '700'

        # размер шрифта полной цены
        item_font_size_price = self.driver.find_element(By.CSS_SELECTOR,
                                                                  ".regular-price").value_of_css_property("font-size")
        assert item_font_size_price == '16px'

        # размер шрифта скидочной цены
        item_font_size_price = self.driver.find_element(By.CSS_SELECTOR,
                                                                  ".campaign-price").value_of_css_property("font-size")
        assert item_font_size_price == '22px'


    #def get_style_home_page(self):


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
