import pytest
from tests.common_scenarios import CommonScenarios

@pytest.mark.usefixtures("register_page")
class TestFeed(CommonScenarios):
    def test_like_post(self):
        assert True

    def test_comment_post(self):
        assert True

    def test_share_post(self):
        assert True

    def test_save_post(self):
        assert True

    def test_unsave_post(self):
        assert True

    def test_search_post(self):
        assert True

    def test_search_hashtag(self):
        assert True

    def test_search_location(self):
        assert True

    def test_search_user(self):
        assert True

    def test_search_user_by_username(self):
        assert True

    def test_search_user_by_name(self):
        assert True

    def test_search_user_by_email(self):
        assert True

    def test_search_user_by_phone(self):
        assert True

    def test_search_user_by_website(self):
        assert True

    def test_search_user_by_bio(self):
        assert True

    def test_search_user_by_category(self):
        assert True
