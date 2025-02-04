from resources.base_class import BaseClass

class LoginPage(BaseClass):
    """"""

    def inst_login(self, username, password):
        """
        Login to the application
        """
        self.set_field(self.loc.input_field.val("username"), username)
        self.set_field(self.loc.input_field.val("password"), password)
        # self.wait_clickable(self.loc.lp_submit_btn).click()
        print("PAUSE HERE")
