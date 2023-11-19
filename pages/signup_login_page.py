from ..pages import base_page, locators
import inspect


class SignupLoginPage(base_page.BasePage):
    # Регистрация нового пользователя
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
        assert self.hover_action(*locators.BasePageLocators.ACCOUNT), \
            "Element 'Аккаунт' is not present"
        assert self.is_element_present(*locators.SignupLoginPageLocators.ALERT_ACCOUNT_TEST), \
            "The element login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_alert_account_vyhod(self):
        assert self.hover_action(*locators.BasePageLocators.ACCOUNT), \
            "Element 'Аккаунт' is not present"
        assert self.is_element_present(*locators.SignupLoginPageLocators.ALERT_ACCOUNT_VYHOD), \
            "The element login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_button_continue(self):
        assert self.click_element(*locators.SignupLoginPageLocators.BUTTON_CONTINUE), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    # Выход из аккаунта
    def click_button_logout(self):
        assert self.hover_action(*locators.BasePageLocators.ACCOUNT), \
            "Element 'Аккаунт' is not present"
        assert self.click_element(*locators.SignupLoginPageLocators.ACCOUNT_VYHOD), \
            "The element MENU_LOGIN is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

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

    # Вход зарегистрированного пользователя
    def click_button_login(self):
        assert self.hover_action(*locators.BasePageLocators.ACCOUNT), \
            "Element 'Аккаунт' is not present"
        assert self.click_element(*locators.BasePageLocators.LOGIN), \
            "The element MENU_LOGIN is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_h1_login(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.H1_LOGIN), \
            "The element login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_h2_login(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.H2_LOGIN), \
            "The element login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def input_email_password(self, email, password):
        assert self.input_data(*locators.SignupLoginPageLocators.LOGIN_INPUT_EMAIL, email), \
            "The element currency is not present"
        assert self.input_data(*locators.SignupLoginPageLocators.LOGIN_INPUT_PASSWORD, password), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_button_login(self):
        assert self.click_element(*locators.SignupLoginPageLocators.BUTTON_LOGIN), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

