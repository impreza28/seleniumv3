from selenium import webdriver
from home_work_19.pages.admin_panel_login_page import AdminPanelLoginPage
from home_work_19.pages.catalog_page import CatalogPage
from home_work_19.pages.item_page import ItemPage
from home_work_19.pages.cart_page import CartPage

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.admin_panel_login_page = AdminPanelLoginPage(self.driver)
        self.catalog_page = CatalogPage(self.driver)
        self.item_page = ItemPage(self.driver)
        self.cart_page = CartPage(self.driver)
    def quit(self):
        self.driver.quit()