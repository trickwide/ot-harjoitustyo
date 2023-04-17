import unittest
from validation.validation import is_username_valid, is_password_valid


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
