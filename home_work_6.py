from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHomeWork():

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_home_work_6(self):
        self.driver.get("http://localhost/litecart/public_html/admin/")

        self.driver.find_element(By.NAME, "username").send_keys('admin')
        self.driver.find_element(By.NAME, "password").send_keys('admin')
        self.driver.find_element(By.NAME, "login").click()

        self.driver.set_window_size(1700, 900)

        menu = list(self.driver.find_elements(By.XPATH, "//li[@id=\'app-\']/a/span[2]"))

        for i in range(len(menu)):
            menu[i].click()
            submenu = list(self.driver.find_elements(By.XPATH, "//ul[@class=\'docs\']/li"))

            if len(submenu) > 0:
                for j in range((len(submenu))-1):
                    submenu[j+1].click()
                    assert len(list(self.driver.find_elements(By.XPATH, "//td[@id='content']/h1"))) == 1
                    #перезаписать подменю
                    submenu = list(self.driver.find_elements(By.XPATH, "//ul[@class=\'docs\']/li"))
            else:
                assert len(list(self.driver.find_elements(By.XPATH, "//td[@id='content']/h1"))) == 1
            # перезаписать меню
            menu = list(self.driver.find_elements(By.XPATH, "//li[@id=\'app-\']/a/span[2]"))
