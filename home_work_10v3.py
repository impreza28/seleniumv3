import re
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test:
    def setup_method(self):

        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://localhost/litecart/public_html/en/')
        self.vars = {}


    def teardown_method(self):
        self.driver.quit()

    def test_check_style(self):
        # главная страница

        name_main = self.driver.find_element(By.CSS_SELECTOR, 'div#box-campaigns div.content div.name').text
        price_old_main = self.driver.find_element(By.CSS_SELECTOR, 'div#box-campaigns div.content s.regular-price').text
        price_new_main = self.driver.find_element(By.CSS_SELECTOR, 'div#box-campaigns div.content strong.campaign-price').text
        color_old_main = self.driver.find_element(By.CSS_SELECTOR,
                                             'div#box-campaigns div.content s.regular-price').value_of_css_property("color")
        style_old_main = self.driver.find_element(By.CSS_SELECTOR,
                                             'div#box-campaigns div.content s.regular-price').value_of_css_property(
            "text-decoration-line")
        color_new_main = self.driver.find_element(By.CSS_SELECTOR,
                                             'div#box-campaigns div.content strong.campaign-price').value_of_css_property(
            "color")
        style_new_main = self.driver.find_element(By.CSS_SELECTOR,
                                             'div#box-campaigns div.content strong.campaign-price').value_of_css_property(
            "font-weight")
        font_old_main = self.driver.find_element(By.CSS_SELECTOR,
                                            'div#box-campaigns div.content s.regular-price').value_of_css_property("font-size")
        font_new_main = self.driver.find_element(By.CSS_SELECTOR,
                                            'div#box-campaigns div.content strong.campaign-price').value_of_css_property(
            "font-size")
        self.driver.find_element(By.CSS_SELECTOR, 'div#box-campaigns a.link').click()

        # страница карточки товара
        name_card = self.driver.find_element(By.CSS_SELECTOR, 'h1.title').text
        price_old_card = self.driver.find_element(By.CSS_SELECTOR, 'div.price-wrapper s.regular-price').text
        price_new_card = self.driver.find_element(By.CSS_SELECTOR, 'div.price-wrapper strong.campaign-price').text
        color_old_card = self.driver.find_element(By.CSS_SELECTOR, 'div.price-wrapper s.regular-price').value_of_css_property(
            "color")
        style_old_card = self.driver.find_element(By.CSS_SELECTOR, 'div.price-wrapper s.regular-price').value_of_css_property(
            "text-decoration-line")
        color_new_card = self.driver.find_element(By.CSS_SELECTOR, 'div.price-wrapper strong.campaign-price').value_of_css_property(
            "color")
        style_new_card = self.driver.find_element(By.CSS_SELECTOR, 'div.price-wrapper strong.campaign-price').value_of_css_property(
            "font-weight")
        font_old_card = self.driver.find_element(By.CSS_SELECTOR, 'div.price-wrapper s.regular-price').value_of_css_property(
            "font-size")
        font_new_card = self.driver.find_element(By.CSS_SELECTOR, 'div.price-wrapper strong.campaign-price').value_of_css_property(
            "font-size")

        # а) на главной странице и на странице товара совпадает текст названия товара

        assert name_main == name_card, 'Названия не совпадают'

        # б) на главной странице и на странице товара совпадают цены (обычная и акционная)

        assert price_old_main == price_old_card, 'Неакционные  цены  не совпадают'

        assert price_new_main == price_new_card, 'Акционные цены не совпадают'

        # обычная цена зачёркнутая и серая (можно считать, что "серый" цвет это такой, у которого в RGBa представлении одинаковые значения для каналов R, G и B)

        assert style_old_main == 'line-through', 'Обычная цена на главной зачеркнута'

        assert style_old_card == 'line-through','Обычная цена в карточке зачеркнута'

        rgb = re.findall(r'\d+', color_old_main)
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]

        assert r == g and g == b and r == b, 'Обычная цена на главной не серая'

        rgb2 = re.findall(r'\d+', color_old_card)
        r2 = rgb2[0]
        g2 = rgb2[1]
        b2 = rgb2[2]

        assert r2 == g2 and g2 == b2 and r2 == b2,'Обычная цена в карточке не серая'

        assert int(style_new_main) >= 700,'Акционная цена на главной не жирная'

        assert int(style_new_card) >= 700, 'Акционная цена в карточке не жирная'

        # г) акционная жирная и красная (можно считать, что "красный" цвет это такой, у которого в RGBa представлении каналы G и B имеют нулевые значения)
        rgb3 = re.findall(r'\d+', color_new_main)
        r3 = int(rgb3[0])
        g3 = int(rgb3[1])
        b3 = int(rgb3[2])

        assert g3 == 0 and b3 == 0, 'Акционная цена на главной красная'

        rgb4 = re.findall(r'\d+', color_new_card)
        r4 = int(rgb4[0])
        g4 = int(rgb4[1])
        b4 = int(rgb4[2])

        assert g4 == 0 and b4 == 0, 'Акционная цена в карточке красная'

        # д) акционная цена крупнее, чем обычная (это тоже надо проверить на каждой странице независимо)
        mfont_old = re.findall(r'\d+', font_old_main)
        mfont_new = re.findall(r'\d+', font_new_main)

        assert int(mfont_old[0]) < int(mfont_new[0]), 'Обычная цена на главной крупнее'

        cfont_old = re.findall(r'\d+', font_old_card)
        cfont_new = re.findall(r'\d+', font_new_card)

        assert int(cfont_old[0]) < int(cfont_new[0]), 'Обычная цена в карточке крупнее'
