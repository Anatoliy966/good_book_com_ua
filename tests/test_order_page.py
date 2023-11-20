import pytest
from ..pages.base_page import BasePage
from ..pages.order_page import OrderPage
from ..pages.signup_login_page import SignupLoginPage
from ..settings import sets

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order_page
class TestOrderPage:

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_login_to_cabinet(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupLoginPage(browser, self.link_to_cabinet)
        page.click_button_login()
        page.explicit_wait(3)
        page.is_h1_login()
        page.is_h2_login()
        page.input_email_password(sets.TEST_EMAIL, sets.PASSWORD)
        page.explicit_wait(5)
        page.press_button_login()
        page.is_alert_account_test()
        page.explicit_wait(5)
        page.is_alert_account_vyhod()
        page.explicit_wait(5)

    def test_add_products_to_cart(self, browser):
        self.link_to_cabinet = browser.current_url
        page = OrderPage(browser, self.link_to_cabinet)
        page.add_to_card_product_1()
        page.explicit_wait(3)
        page.press_btn_prodovjyty_1()
        page.explicit_wait(2)
        page.add_to_card_product_2()
        page.explicit_wait(3)
        page.press_btn_prodovjyty_2()
        page.explicit_wait(3)
        page.add_to_card_product_3()
        page.explicit_wait(5)
        page.press_btn_prodovjyty_3()
        page.explicit_wait(3)
        page.to_card()
        page.explicit_wait(5)
        # page.is_delete_product_2()
        # page.explicit_wait(5)
        page.is_press_button_checkout()
        page.explicit_wait(5)
        page.is_alert_order()
        page.is_press_button_poshta()

        page.is_press_search_city()
        page.explicit_wait(3)
        page.input_field_search_city(sets.FIELD_SEARCH_CITY)
        page.explicit_wait(3)
        page.is_press_search_city_result()
        page.explicit_wait(3)
        page.is_press_search_viddilennya()
        page.explicit_wait(3)
        page.is_press_select_search_poshta()
        page.explicit_wait(3)
        page.is_press_button_pislyaoplata()
        page.explicit_wait(5)
        page.is_press_button_oformyty_zamovl()
        page.explicit_wait(10)

    #
    # def test_in_cart_and_checkout(self, browser):
    #     self.link_to_cabinet = browser.current_url
    #     page = OrderPage(browser, self.link_to_cabinet)
    # #    global price_1_product
    # #    price_1_product = page.add_to_cart_first_product()
    #     page.is_del_1_product_in_cart()
    #     page.is_change_quantity_2_product()
    #     page.explicit_wait(3)
    #     page.is_press_button_update_cart()
    #     page.is_press_button_checkout()
    #     page.explicit_wait(15)
    #
    #     page.is_press_button_post()
    #     page.is_press_city_search()
    #     page.input_search_field_city(sets.SEARCH_FIELD_CITY)
    #     page.explicit_wait(3)
    #     page.is_press_city_result_search()
    #     page.is_press_placeholder_search()
    #     page.explicit_wait(3)
    #     page.is_press_selected_placeholder()
    #     page.is_press_button_postpaid()
    #     page.explicit_wait(5)
    #     page.is_press_button_place_order()
    #     page.explicit_wait(10)
    #
