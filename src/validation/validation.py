import re
from database.database import create_connection, get_user, hash_password


def is_username_valid(username):
    """
    Function to check if the username is valid.

    Args:
        username (str): The username to be validated.

    Returns:
        bool: True if the username is valid, False otherwise.
    """
    return len(username) >= 4


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


def validate_login(username,
                   password,
                   show_main_window,
                   display_error_message,
                   destroy):
    """
    Function to validate the user's login credentials.

    Args:
        username (str): The user's username.
        password (str): The user's password.
        show_main_window (callable): The function to call if login is successful.
        display_error_message (callable): The function to call to display an error message.
        destroy (callable): The function to call to destroy the current view.
    """

    if not username or not password:
        display_error_message("Both username and password are required")
        return

    # Hash the password
    password_hash = hash_password(password)

    # Create a connection to the database
    conn = create_connection("budget_tracker.db")

    # Get the user from the database
    user = get_user(conn, username, password_hash)

    # If the user exists and password is correct, show the main window
    if user:
        user_id = user[0]
        show_main_window(user_id)
        destroy()
    else:
        display_error_message("Invalid username or password")
