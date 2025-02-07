from resources.pages.common_page import CommonPage


class LoginPage(CommonPage):
    """
    Class for Login Page functionality
    """

    def inst_login(self, username, password):
        """
        Login to the application
        """
        self.close_cookie_wnd()
        self.set_field(self.loc.input_field.val("username"), username)
        self.set_field(self.loc.input_field.val("password"), password)
        self.wait_clickable(self.loc.lp_submit_btn).click()

    def close_cookie_wnd(self):
        """
        Close cookie window
        """
        dialog_wnd = self.driver.find_elements(*self.loc.dialog_wnd)
        if dialog_wnd:
            allow_all = dialog_wnd[0].find_element(*self.loc.allow_all_btn)
            allow_all.click()
