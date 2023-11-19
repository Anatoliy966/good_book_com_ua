import pytest
from ..pages.base_page import BasePage
from ..pages.signup_login_page import SignupLoginPage
from ..pages.main_page import MainPage
from ..settings import sets
import random


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.signup_login_logout
class TestSignupLoginLogautPage:
    def setup_method(self):
        hash_name = "%064x" % random.getrandbits(128)
        self.email_for_register = f"{hash_name}@mail.com"
        self.password_for_register = "Qwerty54321"
        self.firstname_for_register = "test"
        self.lastname_for_register = "tests"
        self.phone_for_register = "+380501234567"

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_signup_page(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupLoginPage(browser, self.link_to_cabinet)
        page.click_button_register()
        page.explicit_wait(5)
        page.is_h1_registration()
        page.is_your_personal_data()
        page.input_firstname_lastname_email(self.firstname_for_register, self.lastname_for_register, self.email_for_register)
        page.explicit_wait(5)
        page.is_contact_information()
        page.input_phone(self.phone_for_register)
        page.is_your_password()
        page.input_password(self.password_for_register)
        page.explicit_wait(5)
        page.press_button_register()
        page.is_alert_register()
        page.explicit_wait(5)
        page.is_alert_account_test()
        page.explicit_wait(5)
        page.is_alert_account_vyhod()
        page.explicit_wait(5)
        page.press_button_continue()
        page.explicit_wait(5)

    def test_logout_page(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupLoginPage(browser, self.link_to_cabinet)
        page.click_button_logout()
        page.explicit_wait(3)
        page.is_button_register()
        page.is_button_login()
        page.explicit_wait(3)

    def test_login_page(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupLoginPage(browser, self.link_to_cabinet)
        page.click_button_login()
        page.explicit_wait(5)
        page.is_h1_login()
        page.is_h2_login()
        page.input_email_password(sets.TEST_EMAIL, sets.PASSWORD)
        page.explicit_wait(5)
        page.press_button_login()
        page.is_alert_account_test()
        page.explicit_wait(5)
        page.is_alert_account_vyhod()
        page.explicit_wait(5)

