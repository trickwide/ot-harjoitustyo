import re


def is_username_valid(username):
    """Function to check if the username is valid."""
    return len(username) >= 4


def is_password_valid(password):
    """Function to check if the password is valid."""
    if len(password) < 12:
        return False

    has_uppercase = any(c.isupper() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    return has_uppercase and has_number and has_special
