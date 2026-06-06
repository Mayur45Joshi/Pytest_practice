import pytest
from pages.login_page import LoginPage
from pages.logged_in_page import LoggedInPage


class TestLogin:

    # ────────────────────────────────────────────────
    # TC1: Positive Login
    # ────────────────────────────────────────────────
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_valid_login(self, page, test_data):
        """TC1: Valid credentials should log in successfully"""
        user = test_data["valid_user"]

        # Arrange
        login_page = LoginPage(page)
        login_page.open()

        # Act
        login_page.login(user["username"], user["password"])

        # Assert
        logged_in_page = LoggedInPage(page)

        assert logged_in_page.is_logged_in(), \
            "URL should contain 'logged-in-successfully'"

        assert logged_in_page.contains_success_text(), \
            "Page should contain success message"

        assert logged_in_page.is_logout_button_visible(), \
            "Logout button should be visible"

    # ────────────────────────────────────────────────
    # TC2: Invalid Username
    # ────────────────────────────────────────────────
    @pytest.mark.regression
    @pytest.mark.negative
    def test_invalid_username(self, page, test_data):
        """TC2: Invalid username should show error"""
        user = test_data["invalid_username"]

        login_page = LoginPage(page)
        login_page.open()
        login_page.login(user["username"], user["password"])

        assert login_page.is_error_displayed(), \
            "Error message should be visible"

        assert login_page.get_error_message() == user["error"], \
            f"Expected: '{user['error']}'"

    # ────────────────────────────────────────────────
    # TC3: Invalid Password
    # ────────────────────────────────────────────────
    @pytest.mark.regression
    @pytest.mark.negative
    def test_invalid_password(self, page, test_data):
        """TC3: Invalid password should show error"""
        user = test_data["invalid_password"]

        login_page = LoginPage(page)
        login_page.open()
        login_page.login(user["username"], user["password"])

        assert login_page.is_error_displayed(), \
            "Error message should be visible"

        assert login_page.get_error_message() == user["error"], \
            f"Expected: '{user['error']}'"

    # ────────────────────────────────────────────────
    # TC4: Empty Fields
    # ────────────────────────────────────────────────
    @pytest.mark.negative
    def test_empty_credentials(self, page):
        """TC4: Empty fields should not log in"""
        login_page = LoginPage(page)
        login_page.open()
        login_page.login("", "")

        assert login_page.is_error_displayed(), \
            "Error should show for empty credentials"

    # ────────────────────────────────────────────────
    # TC5: Logout after login
    # ────────────────────────────────────────────────
    @pytest.mark.smoke
    def test_logout_after_login(self, page, test_data):
        """TC5: User should be able to logout successfully"""
        user = test_data["valid_user"]

        login_page = LoginPage(page)
        login_page.open()
        login_page.login(user["username"], user["password"])

        logged_in_page = LoggedInPage(page)
        logged_in_page.expect_logout_button()
        logged_in_page.click_logout()

        # After logout, should return to login or home
        assert "practicetestautomation.com" in page.url