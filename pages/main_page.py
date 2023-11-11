from ..pages import base_page, locators
import inspect # после выполнения каждого теста будет печататься ОК


class MainPage(base_page.BasePage):
    def is_button_register(self):
        assert self.hover_action(*locators.BasePageLocators.ACCOUNT), \
            "Element 'Аккаунт' is not present"
        assert self.is_element_present(*locators.BasePageLocators.REGISTER), \
            "Button 'Реєстрація' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_login(self):
        assert self.hover_action(*locators.BasePageLocators.ACCOUNT), \
            "Element 'Аккаунт' is not present"
        assert self.is_element_present(*locators.BasePageLocators.LOGIN), \
                "Button 'Увійти' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_wish_list(self):
        assert self.hover_action(*locators.BasePageLocators.ACCOUNT), \
                "Element 'Аккаунт' is not present"
        assert self.is_element_present (*locators.BasePageLocators.WISH_LIST), \
                "Button 'Список побажань' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_language_ua(self):
        assert self.hover_action(*locators.BasePageLocators.SETTINGS), \
            "Element 'Настройки' is not present"
        assert self.is_element_present(*locators.BasePageLocators.LANGUAGE_UA), \
                "Button 'UA' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_language_ru(self):
        assert self.hover_action(*locators.BasePageLocators.SETTINGS), \
                "Element 'Настройки' is not present"
        assert self.is_element_present (*locators.BasePageLocators.LANGUAGE_RU), \
                "Button 'RU' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_cart_show(self):
        assert self.is_element_present(*locators.BasePageLocators.CART_SHOW), \
                    "Element 'CART_SHOW' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_field(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_FIELD), \
                    "Element 'SEARCH_FIELD' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_button(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_BUTTON), \
                    "Element 'SEARCH_BUTTON' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_logo(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO), \
                    "Element 'LOGO' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_home_page(self):
        assert self.is_element_present(*locators.BasePageLocators.HOME_PAGE), \
                    "Element 'HOME_PAGE' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_oplata_i_dostavka(self):
        assert self.is_element_present(*locators.BasePageLocators.OPLATA_I_DOSTAVKA), \
                    "Element 'OPLATA_I_DOSTAVKA' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_novinki(self):
        assert self.is_element_present(*locators.BasePageLocators.NOVINKI), \
                    "Element 'NOVINKI' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_bestsellery(self):
        assert self.is_element_present(*locators.BasePageLocators.BESTSELLERY), \
                    "Element 'BESTSELLERY' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_kontakty(self):
        assert self.is_element_present(*locators.BasePageLocators.KONTAKTY), \
                    "Element 'KONTAKTY' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_number_telephone(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE), \
                    "Element 'PHONE' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_logo_viber(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO_VIBER), \
                    "Element 'LOGO_VIBER' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_logo_telegram(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO_TELEGRAM), \
                    "Element 'LOGO_TELEGRAM' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_date_time(self):
        assert self.is_element_present(*locators.BasePageLocators.INFO_DATE_TIME), \
                    "Element 'INFO_DATE_TIME' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_date_delivery(self):
        assert self.is_element_present(*locators.BasePageLocators.INFO_DELIVERY), \
                    "Element 'INFO_DELIVERY' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")


