from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators

class TestLogin:
    def test_login_by_button_log_in_to_account_on_main_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOG_IN_ACCOUNT).click()
        driver.find_element(*TestLocators.LOGIN_INPUT_EMAIL).send_keys("polina_evseeva_15_111@yandex.ru")
        driver.find_element(*TestLocators.LOGIN_INPUT_PASSWORD).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOG_IN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_ORDER)
        )

        assert driver.find_element(*TestLocators.LOGIN_BUTTON_ORDER)

    def test_login_by_button_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*TestLocators.LOGIN_BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.LOGIN_INPUT_EMAIL).send_keys("polina_evseeva_15_111@yandex.ru")
        driver.find_element(*TestLocators.LOGIN_INPUT_PASSWORD).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOG_IN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_ORDER)
        )

        assert driver.find_element(*TestLocators.LOGIN_BUTTON_ORDER)

    def test_login_by_button_log_in_on_registration_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOG_IN_ON_REGISTRATION_PAGE).click()
        driver.find_element(*TestLocators.LOGIN_INPUT_EMAIL).send_keys("polina_evseeva_15_111@yandex.ru")
        driver.find_element(*TestLocators.LOGIN_INPUT_PASSWORD).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOG_IN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_ORDER)
        )

        assert driver.find_element(*TestLocators.LOGIN_BUTTON_ORDER)

    def test_login_by_button_log_in_on_forgot_password_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOG_IN_ON_FORGOT_PASSWORD_PAGE).click()
        driver.find_element(*TestLocators.LOGIN_INPUT_EMAIL).send_keys("polina_evseeva_15_111@yandex.ru")
        driver.find_element(*TestLocators.LOGIN_INPUT_PASSWORD).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOG_IN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_ORDER)
        )

        assert driver.find_element(*TestLocators.LOGIN_BUTTON_ORDER)