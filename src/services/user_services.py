from database.database import create_connection, add_user, hash_password, get_user
import re


class UserService:

    @staticmethod
    def is_username_valid(username):
        """
        Function to check if the username is valid.

        Args:
            username (str): The username to be validated.

        Returns:
            bool: True if the username is valid, False otherwise.
        """
        return len(username) >= 5

    @staticmethod
    def is_password_valid(password):
        """
        Function to check if the password is valid.

        Args:
            password (str): The password to be validated.

        Returns:
            bool: True if the password is valid, False otherwise.
        """

        if len(password) < 12:
            return False

        has_uppercase = any(c.isupper() for c in password)
        has_number = any(c.isdigit() for c in password)
        has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

        return has_uppercase and has_number and has_special

    @staticmethod
    def register_user(username, password, password_confirmation):
        """
        Method to register a new user with the given username and password.

        Args:
            username (str): The username for the new user. Must be at least 5 characters long.
            password (str): The password for the new user. Must be at least 12 characters long and contain at least 1 uppercase letter, 1 number, and 1 special character.
            password_confirmation (str): The confirmation of the password. Must match the password.

        Returns:
            tuple: A tuple containing a boolean and a string. The boolean is True if the registration was successful and False otherwise. The string is an error message in case of failure, and None if the registration was successful.
        """

        if not UserService.is_username_valid(username):
            return False, "Username must be at least 5 characters long."

        if not UserService.is_password_valid(password):
            return False, "Password must contain at least 12 characters, with 1 capital letter, 1 number, and 1 special character."

        if password != password_confirmation:
            return False, "Passwords do not match."

        password_hash = hash_password(password)

        conn = create_connection("budget_tracker.db")
        result = add_user(conn, username, password_hash)
        conn.close()

        if result == "UserExists":
            return False, "Username already exists."
        elif result == "Success":
            return True, None

    def validate_user_credentials(username, password):
        """
        Method to validate the user's credentials.

        Args:
            username (str): The user's username.
            password (str): The user's password.

        Returns:
            int: The user's id, if the credentials are valid, None otherwise.
        """

        password_hash = hash_password(password)

        conn = create_connection("budget_tracker.db")

        user = get_user(conn, username, password_hash)

        return user[0] if user else None
