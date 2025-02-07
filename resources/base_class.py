"""Base class for common actions with webdriver"""

from faker import Faker
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from resources.global_variables import GlobalVariables
from resources.locators import Locators
from resources.custom_wait import CustomWait


class BaseClass(CustomWait):
    """
    Base class for work with browser application
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.actions = ActionChains(driver)
        self.glob = GlobalVariables()
        self.loc = Locators()
        self.fake = Faker()

    def set_field(self, locator, value):
        """
        Set value to the field
        """
        field = self.wait_obj_located(locator)
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(value)
        assert (
            field.get_attribute("value") == value
        ), f"Field {locator} is not filled with value {value}"

    @staticmethod
    def get_parent(element):
        """
        Return the parent object of the element
        """
        return element.find_element("xpath", "..")
