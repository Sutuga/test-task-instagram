"""provided basic functionality for tests suites"""

import allure
import pytest
from resources.global_variables import GlobalVariables as gv
from selenium.webdriver import Chrome
from resources.pages.login_page import LoginPage


@allure.title("Inject all class references to the test class")
@pytest.fixture(name="_injector", scope="class")
def injector(request, driver_setup):
    """
    Define modules
    """
    driver: Chrome = driver_setup
    request.cls.driver = driver
    request.cls.login = LoginPage(driver)

@pytest.fixture(scope="class", params=gv.LOGIN_PAGES)
def login_pages(request, _injector):
    """
    Prepare browser for test. Open additional tab.
    """
    r = request.cls
    r.driver.get(request.param)
    close_cookie_wnd(r.driver, r.login)

@pytest.fixture(scope="class")
def register_page(request, _injector):
    """
    Prepare browser for test. Open additional tab.
    """
    r = request.cls
    r.driver.get(gv.REGISTER_PAGE)
    close_cookie_wnd(r.driver, r.login)

def close_cookie_wnd(driver, login):
    """
    Close cookie window
    """
    dialog_wnd = driver.find_elements(*login.loc.dialog_wnd)
    if dialog_wnd:
        allow_all = dialog_wnd[0].find_element(*login.loc.allow_all_btn)
        allow_all.click()