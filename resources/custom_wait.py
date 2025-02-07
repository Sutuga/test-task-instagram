from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CustomWait:
    """
    Class for custom waits functionality
    Also could be present some custom conditions for extending
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_obj_located(self, locator, msg: str = ""):
        """
        Wait and return the web element object
        """
        return self.wait.until(ec.presence_of_element_located(locator), message=msg)

    def wait_visible_located(self, locator, msg: str = ""):
        """
        Wait object (locator) is present and visible in DOM model
        """
        return self.wait.until(ec.visibility_of_element_located(locator), message=msg)

    def wait_clickable(self, locator, msg: str = ""):
        """
        Wait object is clickable
        """
        return self.wait.until(ec.element_to_be_clickable(locator), message=msg)

    def wait_all_elements_located(self, locator):
        """
        Wait and return all located web elements
        """
        return self.wait.until(ec.presence_of_all_elements_located(locator))
