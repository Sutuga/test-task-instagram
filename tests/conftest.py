"""provided basic functionality for tests suites"""

import allure
import pytest

from selenium.webdriver import Chrome
from resources.pages.login_page import LoginPage
from resources.pages.feed_page import FeedPage
from resources.global_variables import GlobalVariables as gv


@allure.title("Inject all class references to the test class")
@pytest.fixture(name="_injector", scope="class")
def injector(request, driver_setup):
    """
    Define modules
    """
    driver: Chrome = driver_setup
    request.cls.driver = driver
    request.cls.login_page = LoginPage(driver)
    request.cls.main_page = FeedPage(driver)
    request.cls.glob = gv


@pytest.fixture(scope="class", params=gv.LOGIN_PAGES)
def login_pages(request, _injector):
    """
    Prepare browser for test. Open additional tab.
    """
    r = request.cls
    r.driver.get(request.param)


@pytest.fixture(scope="class")
def default_login(request, _injector):
    """
    Prepare browser for test. Open additional tab.
    """
    r = request.cls
    r.driver.get(gv.LOGIN_PAGES[0])
    r.login_page.inst_login(
        r.glob.TEST_VALID_USER["mail"], r.glob.TEST_VALID_USER["password"]
    )
    r.main_page.press_not_now()
