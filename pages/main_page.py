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

    def is_cart_show(self):
        assert self.is_element_present(*locators.BasePageLocators.CART_SHOW), \
                    "Element 'CART_SHOW' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    # def is_number_telephon(self):
    #     assert self.is_element_present(*locators.BasePageLocators.PHONE), \
    #                 "Element 'PHONE' is not present"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")
    #
    # def is_button_currency(self):
    #     assert self.is_element_present(*locators.BasePageLocators.CURRENCY), \
    #         "Element 'CURRENCY' is not present"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")
    #
    # def is_button_uah(self):
    #     assert self.click_element(*locators.BasePageLocators.CURRENCY), \
    #         "The element is not present or intractable"
    #     assert self.is_element_present(*locators.BasePageLocators.CURRENCY), \
    #         "The element is not present"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")
    #
    # def is_button_eur(self):
    #     assert self.click_element(*locators.BasePageLocators.CURRENCY), \
    #         "The element is not present or intractable"
    #     assert self.is_element_present(*locators.BasePageLocators.CURRENCY), \
    #         "The element is not present"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")
    #
    # def is_button_usd(self):
    #     assert self.click_element(*locators.BasePageLocators.CURRENCY), \
    #         "The element is not present or intractable"
    #     assert self.is_element_present(*locators.BasePageLocators.CURRENCY), \
    #         "The element is not present"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")
    #

