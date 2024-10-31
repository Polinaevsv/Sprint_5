from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
class TestGoingToPersonalAccount:
    def test_going_to_personal_account_by_button_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*TestLocators.LOGIN_INPUT_EMAIL).send_keys("polina_evseeva_15_111@yandex.ru")
        driver.find_element(*TestLocators.LOGIN_INPUT_PASSWORD).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOG_IN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_ORDER)
        )
        driver.find_element(*TestLocators.LOGIN_BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT_BUTTON_HISTORY_ORDER)
        )

        assert driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON_HISTORY_ORDER)