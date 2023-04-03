import unittest
from ui.registration_screen import RegistrationScreen

class TestRegistrationScreen(unittest.TestCase):
    
    def test_is_username_valid(self):
        registration = RegistrationScreen(None, None)
        
        self.assertTrue(registration.is_username_valid("username"))
        
    def test_is_username_valid_too_short(self):
        registration = RegistrationScreen(None, None)
        
        self.assertFalse(registration.is_username_valid("usr"))
        
    def test_is_password_valid(self):
        registration = RegistrationScreen(None, None)
        
        self.assertTrue(registration.is_password_valid("Password123!"))
        
    def test_is_password_valid_too_short(self):
        registration = RegistrationScreen(None, None)
        
        self.assertFalse(registration.is_password_valid("Pass123!"))
        
    def test_is_password_valid_no_uppercase(self):
        registration = RegistrationScreen(None, None)
        
        self.assertFalse(registration.is_password_valid("password123!"))
        
    def test_is_password_valid_no_number(self):
        registration = RegistrationScreen(None, None)
        
        self.assertFalse(registration.is_password_valid("Password!@#$"))
        
    def test_is_password_valid_no_special_character(self):
        registration = RegistrationScreen(None, None)
        
        self.assertFalse(registration.is_password_valid("Password1234"))
    
    
        