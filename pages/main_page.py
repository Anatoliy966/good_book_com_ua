from ..pages import base_page, locators
import inspect # после выполнения каждого теста будет печататься ОК


class MainPage(base_page.BasePage):
    def is_account_category(self):
        assert self.is_element_present(*locators.BasePageLocators.ACCOUNT), \
            "Element 'Аккаунт' is not present"
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






    def is_slider_wrapper(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDER_WRAPPER), \
            "The element 'SLIDER_WRAPPER' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_cat_hud_literatura(self):
        assert self.is_element_present(*locators.MainPageLocators.CAT_HUD_LITETATURA), \
            "The element 'CAT_HUD_LITETATURA' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_sub_cat_poeziya(self):
        assert self.hover_action(*locators.MainPageLocators.CAT_HUD_LITETATURA), \
            "The element 'CAT_HUD_LITETATURA' is not present"
        assert self.is_element_present(*locators.MainPageLocators.SUB_CAT_POEZIYA), \
            "The element 'SUB_CAT_POEZIYA' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_selection_novinki(self):
        assert self.is_element_present(*locators.MainPageLocators.SELECTION_NOVINKI), \
            "The element 'SELECTION_NOVINKI' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_novinki_3(self):
        assert self.is_element_present(*locators.MainPageLocators.NOVINKI_3), \
            "The element 'NOVINKI_3' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_novinki_show_more(self):
        assert self.is_element_present(*locators.MainPageLocators.NOVINKI_SHOW_MORE), \
            "The element 'NOVINKI_SHOW_MORE' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_selection_hity(self):
        assert self.is_element_present(*locators.MainPageLocators.SELECTION_HITY), \
            "The element 'SELECTION_HITY' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_prev_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_PREV_HITS), \
            "The element 'BUTTON_PREV_HITS' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_next_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_NEXT_HITS), \
            "The element 'BUTTON_NEXT_HITS' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_selection_bestseller(self):
        assert self.is_element_present(*locators.MainPageLocators.SELECTION_BESTSELER), \
            "The element 'SELECTION_BESTSELER' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_prev_bestseller(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_PREV_BESTSELER), \
            "The element 'BUTTON_PREV_BESTSELER' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_next_bestseller(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_NEXT_BESTSELER), \
            "The element 'BUTTON_NEXT_BESTSELER' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_selection_popular_autor(self):
        assert self.is_element_present(*locators.MainPageLocators.SELECTION_POPULAR_AUTOR), \
            "The element 'SELECTION_POPULAR_AUTOR' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_popular_autor_4(self):
        assert self.is_element_present(*locators.MainPageLocators.POPULAR_AUTOR_4), \
            "The element 'POPULAR_AUTOR_4' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_popular_autor_show_more(self):
        assert self.is_element_present(*locators.MainPageLocators.POPULAR_AUTOR_SHOW_MORE), \
            "The element 'POPULAR_AUTOR_SHOW_MORE' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_selection_popular_serii(self):
        assert self.is_element_present(*locators.MainPageLocators.SELECTION_POPULAR_SERII), \
            "The element 'SELECTION_POPULAR_SERII' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_popular_serii_4(self):
        assert self.is_element_present(*locators.MainPageLocators.POPULAR_SERII_4), \
            "The element 'POPULAR_SERII_4' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_popular_serii_show_more(self):
        assert self.is_element_present(*locators.MainPageLocators.POPULAR_SERII_SHOW_MORE), \
            "The element 'POPULAR_SERII_SHOW_MORE' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")




    def is_selection_hity(self):
        assert self.is_element_present(*locators.MainPageLocators.SELECTION_HITY), \
                "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_prev_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_PREV_HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_next_trend(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_NEXT_HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")





