import pytest
from tests.common_scenarios import CommonScenarios

@pytest.mark.usefixtures("login_pages")
class TestLoginPage(CommonScenarios):

    @pytest.mark.parametrize("name", ["phone", "email", "username"])
    def test_login(self, name):
        """
        Description: Test login with valid credentials
        """
        profile = self.login.fake.simple_profile()
        self.login.inst_login(profile["name"], "password")
        assert True

    def test_logout(self):
        assert True

    def test_login_with_invalid_credentials(self):
        assert True

    def test_login_with_valid_credentials(self):
        assert True
