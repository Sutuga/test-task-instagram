from resources.base_class import BaseClass


class CommonPage(BaseClass):
    """
    Class for common pages logic
    """

    def logout(self):
        """
        Logout from the application
        """
        self.wait_clickable(self.loc.settings_btn, "Setting button not clickable").click()
        self.wait_clickable(self.loc.log_out_btn, "Logout button not clickable").click()

    def click_btn_by_icon(self, post, icon_locator):
        """
        Click button by icon, Find the parent clickable element.
        Could be tricky to get actual clickable element
        """
        pass

    def common_usage_for_all_pages(self):
        """
        Common usage for all pages
        """
        pass
