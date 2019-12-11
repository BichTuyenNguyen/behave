from pageobjects.pages.base_page import BasePage
from pageobjects.action.elements import BaseElement
from pageobjects.locators.insurance_page_locator import InsurancePageLocator


class InsurancePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._locator = InsurancePageLocator

    def click_travel_tab(self):
        travel_tab_locator = self._locator.TRAVEL_TAB
        travel_element = BaseElement(travel_tab_locator, self.driver)
        travel_element.click()
