import pytest
from tests.common_scenarios import CommonScenarios


@pytest.mark.usefixtures("login_pages")
class TestLoginPage(CommonScenarios):
    """
    Test suite for test login pages
    """

    @pytest.mark.parametrize("name", ["mail", "username"])  # ideally add "phone" case
    def test_01_login_with_valid_credentials(self, name):
        """
        Verify login with valid credentials.
        User can correctly log in and log out to the application
        """
        profile = self.glob.TEST_VALID_USER
        self.login_page.inst_login(profile[name], profile["password"])
        assert self.login_page.wait_visible_located(
            self.login_page.loc.home_icon,
            f"Main page is not loaded, waiting the {self.login_page.loc.home_icon}",
        )
        self.main_page.logout()
        assert self.login_page.wait_visible_located(
            self.login_page.loc.lp_submit_btn,
            f"Main page is not loaded, waiting the {self.login_page.loc.lp_submit_btn}",
        )

    @pytest.mark.parametrize("name", ["mail", "username"])  # ideally add "phone" case
    def test_02_login_with_invalid_credentials(self, name):
        """
        Test login with invalid credentials
        User can't log in to the application with invalid credentials
        """
        profile = self.login_page.fake.simple_profile()
        password = self.login_page.fake.password(length=9, special_chars=True)
        self.login_page.inst_login(profile[name], password)

        exp_error_msg = (
            "Sorry, your password was incorrect. Please double-check your password."
        )
        assert self.login_page.wait_visible_located(
            self.login_page.loc.div_field_with_text.val(exp_error_msg),
            f"We can`t se the error message {exp_error_msg}",
        )

    def test_03_login_with_empty_credentials(self):
        """
        Test login with empty credentials
        User can`t log in to the application with empty credentials
        """
        self.login_page.close_cookie_wnd()
        submit_btn = self.driver.find_element(*self.login_page.loc.lp_submit_btn)
        assert not submit_btn.is_enabled(), "Submit button is enabled with empty fields"
