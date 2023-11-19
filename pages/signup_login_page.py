from ..pages import base_page, locators
import inspect


class SignupLoginPage(base_page.BasePage):
    def click_button_register(self):
        assert self.hover_action(*locators.BasePageLocators.ACCOUNT), \
            "Element 'Аккаунт' is not present"
        assert self.click_element(*locators.BasePageLocators.REGISTER), \
            "Button 'Реєстрація' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_h1_registration(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.H1_REGISTRATION), \
            "Button login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_your_personal_data(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.YOUR_PERSONAL_DATA), \
            "Button login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def input_firstname_lastname_email(self, firstname, lastname, email):
        assert self.input_data(*locators.SignupLoginPageLocators.REG_INPUT_FIRSTNAME, firstname), \
            "The element currency is not present"
        assert self.input_data(*locators.SignupLoginPageLocators.REG_INPUT_LASTNAME, lastname), \
            "The element currency is not present"
        assert self.input_data(*locators.SignupLoginPageLocators.REG_INPUT_EMAIL, email), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_contact_information(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.CONTACT_INFORMATION), \
            "Button login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def input_phone(self, phone):
        assert self.input_data(*locators.SignupLoginPageLocators.REG_INPUT_PHONE, phone), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_your_password(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.YOUR_PASSWORD), \
            "Button login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def input_password(self, password):
        assert self.input_data(*locators.SignupLoginPageLocators.REG_INPUT_PASSWORD, password), \
            "The element currency is not present"
        assert self.input_data(*locators.SignupLoginPageLocators.REG_INPUT_CONFIRM_PASSWORD, password), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_button_register(self):
        assert self.click_element(*locators.SignupLoginPageLocators.BUTTON_REGISTER), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_alert_register(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.ALERT_REGISTER), \
            "The element login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_alert_account_test(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.ALERT_ACCOUNT_TEST), \
            "The element login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_alert_account_vyhod(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.ALERT_ACCOUNT_VYHOD), \
            "The element login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_button_continue(self):
        assert self.click_element(*locators.SignupLoginPageLocators.BUTTON_CONTINUE), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")


    def click_menu_login(self):
        assert self.hover_action(*locators.BasePageLocators.ACCOUNT), \
            "Element 'Аккаунт' is not present"
        assert self.click_element(*locators.BasePageLocators.MENU_LOGIN), \
            "The element MENU_LOGIN is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_h1_vhod(self):
        assert self.is_element_present(*locators.LoginPageLocators.H1_LOGIN), \
            "The element login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def input_email_password(self, email, password):
        assert self.input_data(*locators.LoginPageLocators.INPUT_EMAIL, email), \
            "The element currency is not present"
        assert self.input_data(*locators.LoginPageLocators.INPUT_PASSWORD, password), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_button_login(self):
        assert self.click_element(*locators.LoginPageLocators.BUTTON_LOGIN), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_logout_in_header(self):
        assert self.hover_action(*locators.BasePageLocators.ACCOUNT), \
            "Element 'Аккаунт' is not present"
        assert self.is_element_present(*locators.BasePageLocators.MENU_LOGOUT), \
            "Button MENU_LOGOUT is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_button_logout(self):
        assert self.hover_action(*locators.BasePageLocators.ACCOUNT), \
            "Element 'Аккаунт' is not present"
        assert self.click_element(*locators.BasePageLocators.MENU_LOGOUT), \
            "Button MENU_LOGOUT is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_menu_login(self):
        assert self.hover_action(*locators.BasePageLocators.ACCOUNT), \
            "Element 'Аккаунт' is not present"
        assert self.is_element_present(*locators.BasePageLocators.MENU_LOGIN), \
            "The element MENU_LOGIN is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    # def input_email_password(self, email, password):
    #     assert self.input_data(*locators.SignupLoginPageLocators.INPUT_EMAIL, email), \
    #         "The element currency is not present"
    #     assert self.input_data(*locators.SignupLoginPageLocators.INPUT_PASSWORD, password), \
    #         "The element currency is not present"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")


    #
    #
    # def is_h1_vhod(self):
    #     assert self.is_element_present(*locators.SignupLoginPageLocators.H1_VHOD), \
    #         "Button login is not present"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")
    #
    # def press_button_login(self):
    #     assert self.click_element(*locators.SignupLoginPageLocators.BUTTON_LOGIN), \
    #         "The element currency is not present or intractable"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")
    #
    # def click_signup(self):
    #     assert self.click_element(*locators.SignupLoginPageLocators.GO_TO_SIGNUP), \
    #         "The element currency is not present or intractable"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")
    #
    # def is_h1_signup(self):
    #     assert self.is_element_present(*locators.SignupLoginPageLocators.H1_SIGNUP), \
    #         "Button login is not present"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")
    #
    # def input_email_password(self, email, password):
    #     assert self.input_data(*locators.SignupLoginPageLocators.INPUT_EMAIL, email), \
    #         "The element currency is not present"
    #     assert self.input_data(*locators.SignupLoginPageLocators.INPUT_PASSWORD, password), \
    #         "The element currency is not present"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")
    #
    # def press_button_signup(self):
    #     assert self.click_element(*locators.SignupLoginPageLocators.BUTTON_SIGNUP), \
    #         "The element currency is not present or intractable"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")
    #
    # def is_alert_success(self):
    #     assert self.is_element_appears_after_while(*locators.BasePageLocators.ALERT_SUCCESS, timeout=5), \
    #         "The element is not present"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")
    #
    # def is_button_logout_in_header(self):
    #     assert self.is_element_present(*locators.BasePageLocators.LOGOUT), \
    #         "Button login is not present"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")
    #
    # def press_button_logout(self):
    #     assert self.click_element(*locators.BasePageLocators.LOGOUT), \
    #         "The element currency is not present or intractable"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")



