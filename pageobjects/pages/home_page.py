from pageobjects.pages.base_page import BasePage
from pageobjects.action.elements import BaseElement
from pageobjects.locators.home_page_locator import HomePageLocator


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._locator = HomePageLocator

    def click_insurance_tab(self):
        insurance_locator = self._locator.INSURANCE_TAB
        insurance_element = BaseElement(insurance_locator, self._driver)
        insurance_element.click()
