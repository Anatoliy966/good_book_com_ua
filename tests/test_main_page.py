import pytest
from ..pages.base_page import BasePage
from ..pages.main_page import MainPage
import random
from ..settings import sets
# Две точки означают абсолютный путь. Без них в виндовс будет ошибка. В линукс - скорее всего их надо будет убрать
# ..settings надо поставить и в base_page.py

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        hash_name = "%032x" % random.getrandbits(128)
        self.email_for_subscribe = f"{hash_name}@mail.com"

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_main_page_header(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_account_category()
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


    def test_main_page_content(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_slider_wrapper()
        page.is_cat_hud_literatura()
        page.is_sub_cat_poeziya()
        page.is_selection_novinki()
        page.is_novinki_3()
        page.is_novinki_show_more()

        page.is_selection_hity()
        page.scroll_page()
        page.is_button_prev_hits()
        page.is_button_next_trend()

        page.is_selection_hity()
        page.is_button_prev_hits()

        page.is_selection_bestseller()
        page.is_button_prev_bestseller()
        page.is_button_next_bestseller()

        page.is_selection_popular_autor()
        page.is_popular_autor_4()
        page.is_popular_autor_show_more()
        page.is_selection_popular_serii()
        page.is_popular_serii_4()
        page.is_popular_serii_show_more()

    def test_main_page_footer(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_subscribe()
        page.is_input_subscribe()
        # page.subscribe_action()













    # def test_login_logout(self, browser):
    #     link_to_site = browser.current_url

