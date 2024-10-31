from selenium.webdriver.common.by import By

class TestLocators:
    REGISTRATION_INPUT_NAME = By.XPATH, "(//input)[1]" #поле "Имя" формы "Регистрация"
    REGISTRATION_INPUT_EMAIL = By.XPATH, "(//input)[2]" #поле "Email" формы "Регистрация"
    REGISTRATION_INPUT_PASSWORD = By.XPATH, "(//input)[3]" #поле "Пароль" формы "Регистрация"
    REGISTRATION_BUTTON_REGISTER = By.XPATH, "//button[text()='Зарегистрироваться']" #кнопка "Зарегистрироваться" формы "Регистрация"
    REGISTRATION_MESSAGE_INVALID_PASSWORD = By.XPATH, "//p[text()='Некорректный пароль']" # сообщение "Некорректный пароль" при регистрации
    LOGIN_BUTTON_LOG_IN_ACCOUNT = By.XPATH, "//button[text()='Войти в аккаунт']" #кнопка "Войти в аккаунт" на главной странице
    LOGIN_INPUT_EMAIL = By.XPATH, "(//input)[1]" #поле "Email" формы "Вход" на странице /login
    LOGIN_INPUT_PASSWORD = By.XPATH, "(//input)[2]" #поле "Пароль" формы "Вход" на странице /login
    LOGIN_BUTTON_LOG_IN = By.XPATH, "//button[text()='Войти']" #кнопка "Войти" формы "Вход" на странице /login
    LOGIN_BUTTON_PERSONAL_ACCOUNT = By.XPATH, "//p[text()='Личный Кабинет']" #кнопка "Личный кабинет" на главной странице
    LOGIN_BUTTON_ORDER = By.XPATH, "//button[text()='Оформить заказ']" #кнопка "Оформить заказ", которая появляется на главной странице после авторизации
    LOGIN_BUTTON_LOG_IN_ON_REGISTRATION_PAGE = By.XPATH, "//a[text()='Войти']" #кнопка "Войти" на странице /register
    LOGIN_BUTTON_LOG_IN_ON_FORGOT_PASSWORD_PAGE = By.XPATH, "//a[text()='Войти']"  # кнопка "Войти" на странице /forgot-password
    PERSONAL_ACCOUNT_BUTTON_HISTORY_ORDER = By.XPATH, "//a[text()='История заказов']" # кнопка "История заказов" на странице /profile
    PERSONAL_ACCOUNT_BUTTON_CONSTRUCTOR = By.XPATH, "//p[text()='Конструктор']" # кнопка "Конструктор" на странице /profile
    PERSONAL_ACCOUNT_LOGO = By.XPATH, "//p[contains(@class,'AppHeader_header__linkText') and text()='Конструктор']" # лого на странице /profile
    PERSONAL_ACCOUNT_BUTTON_LOG_OUT = By.XPATH, "//button[text()='Выход']" # кнопка "Выход" на странице /profile
    CONSTRUCTOR_SAUCES_SECTION = By.XPATH, "//span[text()='Соусы']" # раздел "Соусы" в конструкторе
    CONSTRUCTOR_TOPPINGS_SECTION = By.XPATH, "//span[text()='Начинки']" # раздел "Начинки" в конструкторе
    CONSTRUCTOR_BREAD_SECTION = By.XPATH, "//span[text()='Булки']" # раздел "Булки" в конструкторе
    CONSTRUCTOR_TAB_SAUCES_OPENED = By.XPATH, "//span[./parent::div[contains(@class,'tab_tab_type_current')]][text()='Соусы']" # открытый таб "Соусы"
    CONSTRUCTOR_TAB_TOPPINGS_OPENED = By.XPATH, "//span[./parent::div[contains(@class,'tab_tab_type_current')]][text()='Начинки']"  # открытый таб "Соусы"
    CONSTRUCTOR_TAB_BREAD_OPENED = By.XPATH, "//span[./parent::div[contains(@class,'tab_tab_type_current')]][text()='Булки']"  # открытый таб "Соусы"
