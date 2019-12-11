from pageobjects.pages.base_page import BasePage
from pageobjects.action.elements import DropdownElement, DatePickerElement, BaseElement
from pageobjects.locators.travel_insurance_page_locator import TravelInsurancePageLocator
from pageobjects.locators.share_common_locator import ShareCommonLocator


class TravelInsurancePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._locator = TravelInsurancePageLocator

    def click_and_select_policy_dropdown(self, policy_name):
        dropdown_locator = self._locator.POLICY_TYPE_DROPDOWN
        dropdown_element = DropdownElement(dropdown_locator, self.driver)
        dropdown_element.select_option_by_option_name(policy_name, move_to_element=True)

    def click_and_select_whos_going_dropdown(self, option_name):
        dropdown_locator = self._locator.WHO_GOING_DROPDOWN
        dropdown_element = DropdownElement(dropdown_locator, self.driver)
        dropdown_element.select_option_by_option_name(option_name, move_to_element=True)

    def click_and_select_destination_dropdown(self, option_name):
        dropdown_locator = self._locator.DESTINATION_DROPDOWN
        dropdown_element = DropdownElement(dropdown_locator, self.driver)
        dropdown_element.select_option_by_option_name(option_name, move_to_element=True)

    def click_and_select_start_date(self, date):
        date_picker_locator = self._locator.START_DATE
        date_picker_element = DatePickerElement(date_picker_locator, self.driver)
        date_picker_element.select_date_by_day(date)

    def click_and_select_end_date(self, date):
        date_picker_locator = self._locator.END_DATE
        date_picker_element = DatePickerElement(date_picker_locator, self.driver)
        date_picker_element.select_date_by_day(date)

    def click_show_result_button(self):
        show_result_button_locator = self._locator.SHOW_RESULT_BUTTON
        show_result_button_element = BaseElement(show_result_button_locator, self.driver)
        show_result_button_element.click()

    def wait_for_invisibility_of_loading_icon(self):
        self.driver.wait_for_invisibility_of_element_located(ShareCommonLocator.LOADING_ICON)
