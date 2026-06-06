from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class LoggedInPage(BasePage):

    # Locators
    LOGOUT_BUTTON       = "a.wp-block-button__link"
    SUCCESS_HEADING     = "h1.wp-block-heading"

    SUCCESS_TEXTS = ["Congratulations", "successfully logged in"]

    def __init__(self, page: Page):
        super().__init__(page)

    def is_logged_in(self) -> bool:
        return "logged-in-successfully" in self.get_current_url()

    def is_logout_button_visible(self) -> bool:
        return self.page.locator(self.LOGOUT_BUTTON).is_visible()

    def get_heading_text(self) -> str:
        return self.page.locator(self.SUCCESS_HEADING).inner_text()

    def contains_success_text(self) -> bool:
        content = self.page.content()
        return any(text in content for text in self.SUCCESS_TEXTS)

    def expect_logout_button(self):
        expect(self.page.locator(self.LOGOUT_BUTTON)).to_be_visible()

    def click_logout(self):
        self.page.locator(self.LOGOUT_BUTTON).click()