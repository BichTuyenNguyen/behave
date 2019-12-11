from selenium.webdriver.common.by import By


class TravelInsuranceResultPageLocator(object):
    ALL_CARD_BRAND_NAMES = (By.CSS_SELECTOR, '[data-gb-name="travel-plan"] .name')
    FILTER_VALUES = (By.CSS_SELECTOR, '.results-text small')
