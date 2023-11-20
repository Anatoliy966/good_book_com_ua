from ..pages import base_page, locators
import inspect

class OrderPage(base_page.BasePage):

    # def click_on_logo(self):
    #     assert self.click_element(*locators.BasePageLocators.LOGO_), \
    #         "The element currency is not present or intractable"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def add_to_cart_first_product(self):
        assert self.click_element(*locators.OrderPageLocators.BUTTON_ADD_FIRST_PRODUCT), \
            "The element is not present or intractable"
        price = self.get_text(*locators.OrderPageLocators.PRICE_FIRST_PRODUCT)
        price = int(price.replace(' грн / шт.')) # 1180
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")
    #    print(f" Ціна першого товару - {price}  ")
        if price:
            return price

    def add_to_card_product_1(self):
        assert self.click_element(*locators.OrderPageLocators.BUTTON_ADD_PRODUCT_1), \
            "The element is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def press_btn_prodovjyty_1(self):
        assert self.click_element(*locators.OrderPageLocators.LINK_PRODOVJYTY_1), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")


    def add_to_card_product_2(self):
        assert self.click_element(*locators.OrderPageLocators.BUTTON_ADD_PRODUCT_2), \
            "The element is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def press_btn_prodovjyty_2(self):
        assert self.click_element(*locators.OrderPageLocators.LINK_PRODOVJYTY_2), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def add_to_card_product_3(self):
        assert self.click_element(*locators.OrderPageLocators.BUTTON_ADD_PRODUCT_3), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_btn_prodovjyty_3(self):
        assert self.click_element(*locators.OrderPageLocators.LINK_PRODOVJYTY_3), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def to_card(self):
        assert self.click_element(*locators.OrderPageLocators.BUTTON_CARD), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_delete_product_2(self):
        assert self.click_element(*locators.OrderPageLocators.DELETE_PRODUCT_2), \
            "The element REMOVE_BTN_1_IN_CART is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_button_checkout(self):
        assert self.click_element(*locators.OrderPageLocators.BUTTON_ORDER), \
            "The element BUTTON_CHECKOUT is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_alert_order(self):
        assert self.is_element_present(*locators.OrderPageLocators.ALERT_ORDER), \
            "The element login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")




    def is_press_button_poshta(self):
        assert self.click_element(*locators.OrderPageLocators.BUTTON_POSHTA), \
            "The element BUTTON_POST is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_search_city(self):
        assert self.click_element(*locators.OrderPageLocators.SEARCH_CITY), \
            "The element MENU_CITY_SEARCH is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def input_field_search_city(self, field_city):
        assert self.input_data(*locators.OrderPageLocators.FIELD_SEARCH_CITY, field_city), \
            "The element FIELD_CITY_SEARCH is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_search_city_result(self):
        assert self.click_element(*locators.OrderPageLocators.SELECT_SEARCH_RESULT), \
            "The element SELECT_RESULT_SEARCH is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")



    def is_press_search_viddilennya(self):
        assert self.click_element(*locators.OrderPageLocators.FIELD_SEARCH_VIDDILENNYA), \
            "The element FIELD_PLACEHOLDER_SEARCH is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_select_search_poshta(self):
        assert self.click_element(*locators.OrderPageLocators.SELECT_SEARCH_POSHTA), \
            "The element SELECT_PLACEHOLDER_SEARCH is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_button_pislyaoplata(self):
        assert self.click_element(*locators.OrderPageLocators.PISLYAOPLATA), \
            "The element SELECT_BTN_POSTPAID is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_button_oformyty_zamovl(self):
        assert self.click_element(*locators.OrderPageLocators.BUTTON_OFORMYTY_ZAMOVL), \
            "The element BUTTON_PLACE_AN_ORDER is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")


    def press_btn_view_your_cart(self):     ##################################################
        assert self.click_element(*locators.OrderPageLocators.BTN_VIEW_YOUR_CART), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")




    def is_change_quantity_2_product(self):
        assert self.clear_field(*locators.OrderPageLocators.QUANTITY_SECOND_PRODUCT), \
            "Element 'INPUT_QUANTITY' is not present"
        assert self.input_data(*locators.OrderPageLocators.QUANTITY_SECOND_PRODUCT, 1), \
            "The element is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_button_update_cart(self):
        assert self.click_element(*locators.OrderPageLocators.BUTTON_UPDATE_CART), \
            "The element BUTTON_UPDATE_CART is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")




    def is_alert_checkout(self):
        assert self.is_element_appears_after_while(*locators.OrderPageLocators.ALERT_ORDER_PLACEMENT, timeout=25), \
            "The element ALERT_ORDER_PLACEMENT is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_press_button_post(self):
        assert self.click_element(*locators.OrderPageLocators.BUTTON_POST), \
            "The element BUTTON_POST is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_city_search(self):
        assert self.click_element(*locators.OrderPageLocators.MENU_CITY_SEARCH), \
            "The element MENU_CITY_SEARCH is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def input_search_field_city(self, field_city):
        assert self.input_data(*locators.OrderPageLocators.FIELD_CITY_SEARCH, field_city), \
            "The element FIELD_CITY_SEARCH is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_city_result_search(self):
        assert self.click_element(*locators.OrderPageLocators.SELECT_RESULT_SEARCH), \
            "The element SELECT_RESULT_SEARCH is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_placeholder_search(self):
        assert self.click_element(*locators.OrderPageLocators.FIELD_PLACEHOLDER_SEARCH), \
            "The element FIELD_PLACEHOLDER_SEARCH is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_selected_placeholder(self):
        assert self.click_element(*locators.OrderPageLocators.SELECT_PLACEHOLDER_SEARCH), \
            "The element SELECT_PLACEHOLDER_SEARCH is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_button_postpaid(self):
        assert self.click_element(*locators.OrderPageLocators.SELECT_BTN_POSTPAID), \
            "The element SELECT_BTN_POSTPAID is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_button_place_order(self):
        assert self.click_element(*locators.OrderPageLocators.BUTTON_PLACE_AN_ORDER), \
            "The element BUTTON_PLACE_AN_ORDER is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

