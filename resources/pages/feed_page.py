from resources.pages.common_page import CommonPage


class FeedPage(CommonPage):
    """
    Class for Feed page functionality
    """

    def press_not_now(self):
        """
        Press Not Now button (For new users)
        """
        if self.wait_obj_located(self.loc.not_now_btn):
            self.wait_clickable(
                self.loc.not_now_btn, "Not Now button not clickable"
            ).click()
            self.wait_obj_located(self.loc.post, "Post not on DOM")

    def like_post(self, post):
        """
        Like post
        """
        self.like_unlike_post(post, self.loc.like_icon, "rgba(245, 245, 245, 1)")

    def unlike_post(self, post):
        """
        Unlike post
        """
        self.like_unlike_post(post, self.loc.unlike_icon, "rgba(255, 48, 64, 1)")

    def like_unlike_post(self, post, icon_locator, actual_color):
        """
        Like or unlike post
        """
        icon = post.find_elements(*icon_locator)
        if icon:
            color = icon[0].value_of_css_property("color")
            if color == actual_color:
                self.wait_clickable(icon[0]).click()  # For scroll to element
                self.actions.double_click(post).perform()
            else:
                print("Post is already in state")
        else:
            print("We can`t find the like icon")

    def comment_post(self, post, post_text):
        """
        Comment post
        """
        comment_btn = post.find_element(*self.loc.comment_icon)
        self.wait_clickable(comment_btn, "Comment button not clickable").click()
        text_field = self.wait_visible_located(self.loc.add_comment_field)
        self.wait_clickable(text_field)

        # The test will be work unstable here, because the text_field not fully loaded.
        # We should add explicit or implicit wait here.
        text_field.send_keys(post_text)

        print(f"We added the text - '{post_text}'to the post")
        # We are not post the comment, bu the next the workable example how to do it
        # self.wait_clickable(self.loc.post_btn, "Post button not clickable").click()

    def share_post(self, post):
        """
        Template to the share the post
        """
        pass
