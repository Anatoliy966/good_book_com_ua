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

    FOOTER_SUBSCRIBE = (By.XPATH, "//button[text()='Підписатися']")
    FOOTER_INPUT_SUBSCRIBE = (By.XPATH, "//input[@name='NewsletterEmail']")


    # ALERT_SUCCESS = (By.XPATH, "//div[@id='alert-success']")
    # ALERT_ERROR = (By.XPATH, "//div[@id='alert-error']")

class MainPageLocators:
    SLIDER_WRAPPER = (By.XPATH, "//div[@class='slider-wrapper']")
    CAT_HUD_LITETATURA = (By.XPATH, "//div[@class='category-navigation-list-wrapper']//*[text()='Художня література']")
    SUB_CAT_POEZIYA = (By.XPATH, "//ul[@class='top-menu']//a[@href='/ua/poeziya']")
    SELECTION_NOVINKI = (By.XPATH, "//div[@class='page-body']/div[1]")
    NOVINKI_3 = (By.XPATH, "//div[@class='page-body']/div[1]/div[2]/div[3]")
    NOVINKI_SHOW_MORE = (By.XPATH, "//div[@class='page-body']/div[1]/div[3]/h3")
    SELECTION_HITY = (By.XPATH, "//div[@class='page-body']/div[2]")
    BUTTON_PREV_HITS = (By.XPATH, "//div[@class='jCarouselMainWrapper'][1]//button[@class='slick-prev slick-arrow']")
    BUTTON_NEXT_HITS = (By.XPATH, "//div[@class='jCarouselMainWrapper'][1]//button[@class='slick-next slick-arrow']")

    SELECTION_BESTSELER = (By.XPATH, "//div[@class='page-body']/div[3]")
    BUTTON_PREV_BESTSELER = (By.XPATH, "//div[@class='page-body']/div[3]/div/h2/button[@class='slick-prev slick-arrow']")
    BUTTON_NEXT_BESTSELER = (By.XPATH, "//div[@class='page-body']/div[3]/div/h2/button[@class='slick-next slick-arrow']")

    SELECTION_POPULAR_AUTOR = (By.XPATH, "//div[@class='page-body']/div[5]")
    POPULAR_AUTOR_4 = (By.XPATH, "//div[@class='page-body']/div[5]/div[2]/div[4]")
    POPULAR_AUTOR_SHOW_MORE = (By.XPATH, "//div[@class='page-body']/div[5]/div[3]/h4")

    SELECTION_POPULAR_SERII = (By.XPATH, "//div[@class='page-body']/div[6]")
    POPULAR_SERII_4 = (By.XPATH, "//div[@class='page-body']/div[6]/div[2]/div[2]")
    POPULAR_SERII_SHOW_MORE = (By.XPATH, "//div[@class='page-body']/div[6]/div[3]/h4")


class SignupLoginPageLocators:
    H1_REGISTRATION = (By.XPATH, "//h1[text() = 'Реєстрація']")
    YOUR_PERSONAL_DATA = (By.XPATH, "//strong[text() = 'Ваші особисті дані']")
    REG_INPUT_FIRSTNAME = (By.XPATH, "//input[@name='FirstName']")
    REG_INPUT_LASTNAME = (By.XPATH, "//input[@id='LastName']")
    REG_INPUT_EMAIL = (By.XPATH, "//input[@id='Email']")
    CONTACT_INFORMATION = (By.XPATH, "//*[text()='Контактна інформація']")
    REG_INPUT_PHONE = (By.XPATH, "//input[@name='Phone']")
    YOUR_PASSWORD = (By.XPATH, "//*[text()='Ваш пароль']")
    REG_INPUT_PASSWORD = (By.XPATH, "//input[@name='Password']")
    REG_INPUT_CONFIRM_PASSWORD = (By.XPATH, "//input[@name='ConfirmPassword']")
    BUTTON_REGISTER = (By.XPATH, "//button[@id='register-button']")
    ALERT_REGISTER = (By.XPATH, "//div[text()='Реєстрація завершена']")
    ALERT_ACCOUNT_TEST = (By.XPATH, "//a[text()='test']")
    ALERT_ACCOUNT_VYHOD = (By.XPATH, "//a[text()='Выйти']")
    BUTTON_CONTINUE = (By.XPATH, "//a[text()='Продовжити']")

    ACCOUNT_VYHOD = (By.XPATH, "//a[text()='Выйти']")

    H1_LOGIN = (By.XPATH, "//h1[text()='Ласкаво просимо! Будь ласка, увійдіть.']")
    H2_LOGIN = (By.XPATH, "//strong[text()='Зареєстрований клієнт']")
    LOGIN_INPUT_EMAIL = (By.XPATH, "//input[@class='email']")
    LOGIN_INPUT_PASSWORD = (By.XPATH, "//input[@class='password']")
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Увійти']")


class OrderPageLocators:
    # Покупки
    PRODUCT_1 = (By.XPATH, "//div[@class='product-grid'][1]//div[@class='item-box'][4]")
    BUTTON_ADD_PRODUCT_1 = (By.XPATH, "//div[@class='product-grid'][1]//div[@class='item-box'][4]//span[text() ='У кошик']")
    PRICE_PRODUCT_1 = (By.XPATH, "//strong[@class='price']")
    BUTTON_WRAPPER_1 = (By.XPATH, "//div[@class='k-widget k-window ajaxCart']//button[text()='Оформлення замовлення']")
    LINK_PRODOVJYTY_1 = (By.XPATH, "//div[@class='productAddedToCartWindowSummary']//a[@href='#']")

    PRODUCT_2 = (By.XPATH, "//div[@class='product-grid'][1]//div[@class='item-box'][8]")
    BUTTON_ADD_PRODUCT_2 = (By.XPATH, "//div[@class='product-grid'][1]//div[@class='item-box'][8]//span[text() ='У кошик']")
    PRICE_PRODUCT_2 = (By.XPATH, "//strong[@class='price']")
    BUTTON_WRAPPER_2 = (By.XPATH, "//div[@class='k-widget k-window ajaxCart']//button[text()='Оформлення замовлення']")
    LINK_PRODOVJYTY_2 = (By.XPATH, "//div[@class='productAddedToCartWindowSummary']//a[@href='#']")

    POP_AUTOR = (By.XPATH, "//img[@alt='Книги Пастуро Мишель']")
    ALERT_POP_AUTOR = (By.XPATH, "//h1[text()='Книги автора Пастуро Мішель']")
    PRODUCT_3 = (By.XPATH, "//div[@class='product-grid']//div[@class='item-box'][5]")
    BUTTON_ADD_PRODUCT_3 = (By.XPATH, "//div[@class='product-grid'][1]//div[@class='item-box'][5]//span[text() ='У кошик']")
    PRICE_PRODUCT_3 = (By.XPATH, "//strong[@class='price']")
    BUTTON_WRAPPER_3 = (By.XPATH, "//div[@class='k-widget k-window ajaxCart']//button[text()='Оформлення замовлення']")
    LINK_PRODOVJYTY_3 = (By.XPATH, "//div[@class='productAddedToCartWindowSummary']//a[@href='#']")

    BUTTON_CARD = (By.XPATH, "//div[@class='flyout-cart-wrapper']")

    DELETE_PRODUCT_2 = (By.XPATH, "//td[@class='remove-from-cart']//input[@name='removefromcart']")
    ALERT_CARD = (By.XPATH, "//div[@class='flyout-cart-wrapper']//span[text()='(2)']")

    # Оформлення замовлення
    BUTTON_ORDER = (By.XPATH, "//div[@class='checkout-buttons']//button[@class='button-1 checkout-button']")
    ALERT_ORDER = (By.XPATH, '//div[@class="page-title"]')
    BUTTON_POSHTA = (By.XPATH, '//input[@value="post"]')
    SEARCH_CITY = (By.XPATH, '//span[@aria-labelledby="select2-js-data-example-ajax-container"]')
    FIELD_SEARCH_CITY = (By.XPATH, '//input[@class="select2-search__field"]')
    SELECT_SEARCH_RESULT = (By.XPATH, '//ul[@class="select2-results__options"]')
    FIELD_SEARCH_VIDDILENNYA = (By.XPATH, '//span[@class="select2-selection__placeholder"]')
    SELECT_SEARCH_POSHTA = (By.XPATH, '//li[@class="select2-results__option"][4]')
    PISLYAOPLATA = (By.XPATH, '//input[@id="paymentmethod_1"]')
    BUTTON_OFORMYTY_ZAMOVL = (By.XPATH, '//button[@data-complete="Оформити замовлення"]')


class WishListLocators:
    # Список побажань
    SPYSOK_POBAJAN = (By.XPATH, "//div[@class='product-grid'][1]//div[@class='item-box'][6]//button[text() ='Додати до списку побажань']")
    BUTTON_SPYSOK_POBAJAN = (By.XPATH, "//div[@class='k-widget k-window ajaxCart']//button[text()='Список побажань']")
    ALERT_LIST_SPYSOK_POBAJAN = (By.XPATH, "//div[@class='master-column-wrapper']//h1[text()='Список побажань']")
    ALERT_ACCOUNT = (By.XPATH, "//div[@class='header-links']//span[text()='Список побажань']")
    BUTTON_DELETE_POBAJAN = (By.XPATH, "//td[@class='remove-from-cart']//input[@aria-label='прибрати']")
    ALERT_LIST_POBAJAN = (By.XPATH, "//div[@class='master-column-wrapper']//div[@class='no-data']")


class CabinetPageLocators:
    pass


class CategoryPageLocators:
    pass


class SearchPageLocators:
    pass
