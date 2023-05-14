import unittest
from services.user_services import UserService
from database.database import create_connection, add_user, hash_password, get_user, create_tables


class TestUserService(unittest.TestCase):

    def setUp(self):
        self.conn = create_connection(":memory:")
        create_tables(self.conn)

    def tearDown(self):
        self.conn.close()

    def test_is_username_valid(self):
        self.assertTrue(UserService.is_username_valid("username"))

    def test_is_username_valid_too_short(self):
        self.assertFalse(UserService.is_username_valid("usr"))

    def test_is_password_valid(self):
        self.assertTrue(UserService.is_password_valid("Password123!"))

    def test_is_password_valid_too_short(self):
        self.assertFalse(UserService.is_password_valid("Pass123!"))

    def test_is_password_valid_no_uppercase(self):
        self.assertFalse(UserService.is_password_valid("password123!"))

    def test_is_password_valid_no_number(self):
        self.assertFalse(UserService.is_password_valid("Password!@#$"))

    def test_is_password_valid_no_special_character(self):
        self.assertFalse(UserService.is_password_valid("Password1234"))

    def test_register_user_too_short_username(self):
        result = UserService.register_user(
            "usr", "Password123!", "Password123!")
        self.assertEqual(
            (False, 'Username must be at least 5 characters long.'), result)

    def test_register_user_invalid_password(self):
        result = UserService.register_user(
            "username", "Password123", "Password123")
        self.assertEqual(
            (False, 'Password must contain at least 12 characters, with 1 capital letter, 1 number, and 1 special character.'), result)

    def test_register_user_passwords_dont_match(self):
        result = UserService.register_user(
            "username", "Password123!", "Password123")
        self.assertEqual((False, 'Passwords do not match.'), result)

    def test_register_user_username_already_exists(self):
        result = UserService.register_user(
            "username", "Password123!", "Password123!")
        self.assertEqual((False, "Username already exists."), result)

    def test_register_user_success(self):
        result = UserService.register_user(
            "username", "Password123!", "Password123!")
        self.assertEqual((True, None), result)
