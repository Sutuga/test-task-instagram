from selenium.webdriver.common.by import By


class Dynamic:
    """
    Using for dynamically changing locators by sending value.
    By default, we will use the mask "dynamic-test-value" for the locator.
    The value will be inserted in the mask "dynamic-test-value""
    """

    mask = "dynamic-test-value"

    def __init__(self, way, locator):
        self.way = way
        self.locator = locator

    def val(self, value):
        """
        Return the locator with the new value
        """
        return self.way, self.locator.replace(self.mask, value)


class Locators:
    """
    All locators for the project
    """

    # General
    input_field = Dynamic(By.CSS_SELECTOR, "input[name='dynamic-test-value']")
    div_field_with_text = Dynamic(
        By.XPATH, "//div[normalize-space()='dynamic-test-value']"
    )

    # Dialog window
    dialog_wnd = (By.CSS_SELECTOR, "div[role='dialog']")
    allow_all_btn = (By.XPATH, "//button[text()='Allow all cookies']")
    decline_optional_btn = (By.XPATH, "//button[text()='Decline optional cookies']")

    # Login page
    lp_submit_btn = (By.CSS_SELECTOR, "button[type='submit']")

    # Main page
    home_icon = (By.CSS_SELECTOR, "svg[aria-label='Home']")
    main_page = (By.CSS_SELECTOR, "main[role=main]")

    settings_btn = (By.CSS_SELECTOR, "span[aria-describedby=':rb:']")
    log_out_btn = (By.XPATH, "//div[@role='button'][normalize-space()='Log out']")

    # Posts
    not_now_btn = (By.XPATH, "//div[normalize-space()='Not now']")
    post = (By.CSS_SELECTOR, "article")
    like_icon = (By.CSS_SELECTOR, "div[role='button'] svg[aria-label='Like']")
    unlike_icon = (By.CSS_SELECTOR, "div[role='button'] svg[aria-label='Unlike']")
    comment_icon = (By.CSS_SELECTOR, "div[role='button'] svg[aria-label='Comment']")
    share_icon = (By.CSS_SELECTOR, "div[role='button'] svg[aria-label='Share Post']")

    add_comment_field = (By.CSS_SELECTOR, "div[role='dialog'] [aria-label~='Add']")
    post_btn = (
        By.XPATH,
        "//div[@role='dialog']//div[@role='button'][normalize-space()='Post']",
    )
