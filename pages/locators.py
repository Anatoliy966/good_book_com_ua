from selenium.webdriver.common.by import By


class BasePageLocators:
    ACCOUNT = (By.XPATH, "//label[text()='Аккаунт']")
    REGISTER = (By.XPATH, "//a[text()='Реєстрація']")
    LOGIN = (By.XPATH, "//a[text()='Увійти']")
    WISH_LIST = (By.XPATH, "//a[text()='Список побажань']")
    CART_SHOW = (By.XPATH, "//a[@class='cart-trigger']")
    SETTINGS = (By.XPATH, "//label[text()='Настройки']")
    LANGUAGE_UA = (By.XPATH, "//option[text()='UA']")
    LANGUAGE_RU = (By.XPATH, "//option[text()='Ru']")
    SEARCH_FIELD = (By.XPATH, "//input[@id='small-searchterms']")
    SEARCH_BUTTON = (By.XPATH, "//button[text()='Пошук']")
    LOGO = (By.XPATH, "//a[@class='logo']")
    HOME_PAGE = (By.XPATH, "//a[text()='Головна']")
    OPLATA_I_DOSTAVKA = (By.XPATH, "//ul[@class='top-menu']//a[text()='Оплата і доставка']")
    NOVINKI = (By.XPATH, "//ul[@class='top-menu']//a[text()='Новинки']")
    BESTSELLERY = (By.XPATH, "//ul[@class='top-menu']//a[text()='Бестселери']")
    KONTAKTY = (By.XPATH, "//ul[@class='top-menu']//a[text()='Контакти']")
    PHONE = (By.XPATH, "//div[@class='admin-header-links my-modile']//a[@href='tel:+380739387943']")
    LOGO_VIBER = (By.XPATH, "//a[@class='social-logo viber']")
    LOGO_TELEGRAM = (By.XPATH, "//a[@class='social-logo telegram']")
    INFO_DATE_TIME = (By.XPATH, "//div[@class='admin-header-links my-modile']//span[text()='Вт-Вс 10:00-16:00']")
    INFO_DELIVERY = (By.XPATH, "//div[@class='admin-header-links my-modile']//span[text()='Доставка по всей Украине']")

class MainPageLocators:
    SLIDER_WRAPPER = (By.XPATH, "//div[@class='slider-wrapper']")
    CAT_HUD_LITETATURA = (By.XPATH, "//div[@class='category-navigation-list-wrapper']//a[@href='/ua/hudozhnya-literatura']")
    SUB_CAT_POEZIYA = (By.XPATH, "//ul[@class='top-menu']//a[@href='/ua/poeziya']")

    SELECTION_NOVINKI = (By.XPATH, "//div[@class='page-body']/div[1]")
    NOVINKI_3 = (By.XPATH, "//div[@class='page-body']/div[1]/div[2]/div[3]")
    NOVINKI_SHOW_MORE = (By.XPATH, "//div[@class='page-body']/div[1]/div[3]/h3")

    SELECTION_HITY = (By.XPATH, "//div[@class='page-body']/div[2]")
    BUTTON_PREV_HITS = (By.XPATH, "//div[@class='page-body']/div[2]/div/h2/button[@class='slick-prev slick-arrow']")
    BUTTON_NEXT_HITS = (By.XPATH, "//div[@class='page-body']/div[2]/div/h2/button[@class='slick-next slick-arrow']")

    SELECTION_BESTSELER = (By.XPATH, "//div[@class='page-body']/div[3]")
    BUTTON_PREV_BESTSELER = (By.XPATH, "//div[@class='page-body']/div[3]/div/h2/button[@class='slick-prev slick-arrow']")
    BUTTON_NEXT_BESTSELER = (By.XPATH, "//div[@class='page-body']/div[3]/div/h2/button[@class='slick-next slick-arrow']")

    SELECTION_POPULAR_AUTOR = (By.XPATH, "//div[@class='page-body']/div[5]")
    POPULAR_AUTOR_4 = (By.XPATH, "//div[@class='page-body']/div[5]/div[2]/div[4]")
    POPULAR_AUTOR_SHOW_MORE = (By.XPATH, "//div[@class='page-body']/div[5]/div[3]/h4")

    SELECTION_POPULAR_SERII = (By.XPATH, "//div[@class='page-body']/div[6]")
    POPULAR_SERII_4 = (By.XPATH, "//div[@class='page-body']/div[6]/div[2]/div[2]")
    POPULAR_SERII_SHOW_MORE = (By.XPATH, "//div[@class='page-body']/div[6]/div[3]/h4")
