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
