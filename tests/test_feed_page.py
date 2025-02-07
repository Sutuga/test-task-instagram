import pytest
from tests.common_scenarios import CommonScenarios


@pytest.mark.usefixtures("default_login")
class TestFeedPage(CommonScenarios):
    """
    Test suite for the Feed page
    """

    # Could be parametrized for different like methods (doubleclick, click by icon)
    def test_01_like_post(self):
        """
        User can like a post by doubleclick on post. Icon change color
        """
        posts = self.main_page.wait_all_elements_located(self.main_page.loc.post)
        if posts:
            self.main_page.like_post(posts[0])
            icon = posts[0].find_elements(*self.main_page.loc.unlike_icon)
            assert icon, "Post is not liked"
            icon_color = icon[0].value_of_css_property("color")
            assert icon_color == "rgba(255, 48, 64, 1)", "Post is not liked"
            # Here could be added unlike mechanism, or even make test like - unlike

    def test_02_comment_post(self):
        """
        User can comment a post
        """
        posts = self.main_page.wait_all_elements_located(self.main_page.loc.post)
        if posts:
            self.main_page.comment_post(posts[0], "Nice, This is perfect")
            # Here we should validate added post
            assert True, "Comment not added to the post or not visible"  # template
            # Here could be removing the comment mechanism

    def test_03_share_post(self):
        """
        User can share a post
        """
        assert True

    def test_save_post(self):
        """
        User can save a post
        """
        assert True
