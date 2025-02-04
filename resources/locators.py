"""All locators"""

from selenium.webdriver.common.by import By


class Dynamic:
    """
    Using for dynamically changing locators by sending value.
    By default, we will use the mask "dynamic-test-value" for the locator.
    The value will be inserted in the mask "dynamic-test-value""
    """

    mask = "dynamic-test-value"

    def __init__(self, way, locator):
        self.way = way
        self.locator = locator

    def val(self, value):
        return self.way, self.locator.replace(self.mask, value)


class Locators:
    """All locators for the project"""

    # General
    input_field = Dynamic(By.CSS_SELECTOR, "input[name='dynamic-test-value']")

    # Dialog window
    dialog_wnd = (By.CSS_SELECTOR, "div[role='dialog']")
    allow_all_btn = (By.XPATH, "//button[text()='Allow all cookies']")
    decline_optional_btn = (By.XPATH, "//button[text()='Decline optional cookies']")

    # Login page
    lp_submit_btn = (By.CSS_SELECTOR, "button[type='submit']")