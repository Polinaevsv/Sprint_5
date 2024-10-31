from locators import TestLocators
class TestConstructor:
    def test_going_to_sauces_section_in_constructor(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*TestLocators.CONSTRUCTOR_SAUCES_SECTION).click()

        assert driver.find_element(*TestLocators.CONSTRUCTOR_TAB_SAUCES_OPENED)

    def test_going_to_toppings_section_in_constructor(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*TestLocators.CONSTRUCTOR_TOPPINGS_SECTION).click()

        assert driver.find_element(*TestLocators.CONSTRUCTOR_TAB_TOPPINGS_OPENED)

    def test_going_to_breads_section_in_constructor(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*TestLocators.CONSTRUCTOR_TOPPINGS_SECTION).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BREAD_SECTION).click()

        assert driver.find_element(*TestLocators.CONSTRUCTOR_TAB_BREAD_OPENED)