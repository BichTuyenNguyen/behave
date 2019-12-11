from pageobjects.pages.base_page import BasePage
from pageobjects.action.elements import BaseElement
from pageobjects.locators.travel_insurance_result_page_locator import TravelInsuranceResultPageLocator


class TravelInsuranceResultPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._locator = TravelInsuranceResultPageLocator

    def get_all_card_brand_names(self):
        elements = self.driver.wait_for_elements_to_be_presented(
            self._locator.ALL_CARD_BRAND_NAMES)
        return [element.text for element in elements]

    def get_filter_overview_values(self):
        element = BaseElement(self._locator.FILTER_VALUES, self.driver)
        return element.get_text()
