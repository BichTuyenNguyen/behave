from selenium.webdriver.common.by import By


class ShareCommonLocator(object):
    DROPDOWN_OPTION = (By.XPATH, '(//span[text()="{option_name}"]/parent::a/parent::li)[1]')
    DATE_OPTION = (By.XPATH, '//td[contains(@class, "day")][text()="{day}"]')
    LOADING_ICON = (By.CLASS_NAME, 'uil-rolling-css')
