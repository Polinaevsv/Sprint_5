from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators

class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.REGISTRATION_INPUT_NAME).send_keys("Полина")
        driver.find_element(*TestLocators.REGISTRATION_INPUT_EMAIL).send_keys("polina_evseeva_15_117@yandex.ru")
        driver.find_element(*TestLocators.REGISTRATION_INPUT_PASSWORD).send_keys("123456")
        driver.find_element(*TestLocators.REGISTRATION_BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_LOG_IN)
        )

        assert driver.find_element(*TestLocators.LOGIN_BUTTON_LOG_IN)

    def test_unsuccessful_registration_password_is_five_simbols(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.REGISTRATION_INPUT_NAME).send_keys("Полина")
        driver.find_element(*TestLocators.REGISTRATION_INPUT_EMAIL).send_keys("polina_evseeva_15_221@yandex.ru")
        driver.find_element(*TestLocators.REGISTRATION_INPUT_PASSWORD).send_keys("12345")
        driver.find_element(*TestLocators.REGISTRATION_BUTTON_REGISTER).click()

        assert driver.find_element(*TestLocators.REGISTRATION_MESSAGE_INVALID_PASSWORD)