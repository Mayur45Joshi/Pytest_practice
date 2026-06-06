from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from utils.config import BASE_URL


class LoginPage(BasePage):

    # Locators
    USERNAME_INPUT   = "#username"
    PASSWORD_INPUT   = "#password"
    SUBMIT_BUTTON    = "#submit"
    ERROR_MESSAGE    = "#error"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        self.navigate(BASE_URL)

    def enter_username(self, username: str):
        self.page.fill(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self.page.fill(self.PASSWORD_INPUT, password)

    def click_submit(self):
        self.page.click(self.SUBMIT_BUTTON)

    def login(self, username: str, password: str):
        """Full login action"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()

    def get_error_message(self) -> str:
        return self.page.locator(self.ERROR_MESSAGE).inner_text()

    def is_error_displayed(self) -> bool:
        return self.page.locator(self.ERROR_MESSAGE).is_visible()

    def expect_error_message(self, expected_text: str):
        expect(self.page.locator(self.ERROR_MESSAGE)).to_be_visible()
        expect(self.page.locator(self.ERROR_MESSAGE)).to_have_text(expected_text)