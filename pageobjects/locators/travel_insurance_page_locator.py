from selenium.webdriver.common.by import By


class TravelInsurancePageLocator(object):
    POLICY_TYPE_DROPDOWN = (By.XPATH, '(//span[@class="filter-option clearfix"])[1]')
    WHO_GOING_DROPDOWN = (By.XPATH, '(//span[@class="filter-option clearfix"])[2]')
    DESTINATION_DROPDOWN = (By.XPATH, '(//span[@class="filter-option clearfix"])[3]')
    START_DATE = (By.NAME, 'startdate')
    END_DATE = (By.NAME, 'enddate')
    SHOW_RESULT_BUTTON = (By.NAME, 'product-form-submit')
