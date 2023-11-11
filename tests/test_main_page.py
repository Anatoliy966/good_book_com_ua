import pytest
from ..pages.base_page import BasePage
from ..pages.main_page import MainPage
from ..settings import sets
# Две точки означают абсолютный путь. Без них в виндовс будет ошибка. В линукс - скорее всего их надо будет убрать
# ..settings надо поставить и в base_page.py

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        pass

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_main_page_header(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_register()
        page.is_button_login()
        page.is_button_wish_list()
        page.is_cart_show()
        page.is_language_ua()
        page.is_language_ru()
        page.is_search_field()
        page.is_search_button()
        page.is_logo()
        page.is_home_page()
        page.is_oplata_i_dostavka()
        page.is_novinki()
        page.is_bestsellery()
        page.is_kontakty()
        page.is_number_telephone()
        page.is_logo_viber()
        page.is_logo_telegram()
        page.is_info_date_time()
        page.is_info_date_delivery()











    # def test_login_logout(self, browser):
    #     link_to_site = browser.current_url

