import unittest
from unittest.mock import MagicMock
from validation.validation import is_username_valid, is_password_valid, validate_login


class TestValidation(unittest.TestCase):

    def test_is_username_valid(self):
        self.assertTrue(is_username_valid("username"))

    def test_is_username_valid_too_short(self):

        self.assertFalse(is_username_valid("usr"))

    def test_is_password_valid(self):

        self.assertTrue(is_password_valid("Password123!"))

    def test_is_password_valid_too_short(self):

        self.assertFalse(is_password_valid("Pass123!"))

    def test_is_password_valid_no_uppercase(self):

        self.assertFalse(is_password_valid("password123!"))

    def test_is_password_valid_no_number(self):

        self.assertFalse(is_password_valid("Password!@#$"))

    def test_is_password_valid_no_special_character(self):

        self.assertFalse(is_password_valid("Password1234"))

    def test_validate_login_valid_credentials(self):
        username = "username"
        password = "Password123!"
        user_id = 1

        # Mock functions
        show_main_window = MagicMock()
        display_error_message = MagicMock()
        destroy = MagicMock()

        # Mock database functions
        get_user_mock = MagicMock(return_value=(user_id, username, password))
        with unittest.mock.patch("validation.validation.get_user", get_user_mock):
            validate_login(username, password, show_main_window,
                           display_error_message, destroy)

        # Check if the main window is shown and the login screen is destroyed
        show_main_window.assert_called_once_with(user_id)
        destroy.assert_called_once()
        display_error_message.assert_not_called()

    def test_validate_login_invalid_credentials(self):
        username = "username"
        password = "Password123!"

        # Mock functions
        show_main_window = MagicMock()
        display_error_message = MagicMock()
        destroy = MagicMock()

        # Mock database functions
        get_user_mock = MagicMock(return_value=None)
        with unittest.mock.patch("validation.validation.get_user", get_user_mock):
            validate_login(username, password, show_main_window,
                           display_error_message, destroy)

        # Check if an error message is displayed
        display_error_message.assert_called_once_with(
            "Invalid username or password")
        show_main_window.assert_not_called()
        destroy.assert_not_called()
        
        def test_validate_login_empty_username(self):
            username = ""
            password = "Password123!"

            # Mock functions
            show_main_window = MagicMock()
            display_error_message = MagicMock()
            destroy = MagicMock()

            validate_login(username, password, show_main_window, display_error_message, destroy)

            # Check if an error message is displayed
            display_error_message.assert_called_once_with("Both username and password are required")
            show_main_window.assert_not_called()
            destroy.assert_not_called()

    def test_validate_login_empty_password(self):
        username = "username"
        password = ""

        # Mock functions
        show_main_window = MagicMock()
        display_error_message = MagicMock()
        destroy = MagicMock()

        validate_login(username, password, show_main_window, display_error_message, destroy)

        # Check if an error message is displayed
        display_error_message.assert_called_once_with("Both username and password are required")
        show_main_window.assert_not_called()
        destroy.assert_not_called()

