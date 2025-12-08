import pytest
from e2eproject.pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self, setup):
        driver = setup
        login_page = LoginPage(driver)

        login_page.open()
        login_page.login("tomsmith", "SuperSecretPassword!")

        message = login_page.get_message()
        assert "You logged into a secure area!" in message, "Login failed!"
