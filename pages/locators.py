from selenium.webdriver.common.by import By


class BasePageLocators:
    ACCOUNT = (By.XPATH, "//*[text()='Аккаунт']")
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
