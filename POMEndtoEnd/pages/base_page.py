from playwright.sync_api import Page, expect
from utils.config import TIMEOUT


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.page.set_default_timeout(TIMEOUT)

    def navigate(self, url: str):
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()

    def get_current_url(self) -> str:
        return self.page.url

    def take_screenshot(self, name: str):
        self.page.screenshot(path=f"screenshots/{name}.png")

    def wait_for_url(self, url_pattern: str):
        self.page.wait_for_url(f"**{url_pattern}**")