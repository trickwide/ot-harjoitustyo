from tkinter import ttk, constants
import customtkinter
import hashlib
from database import create_connection, add_user

class RegistrationScreen:
    """The RegistrationScreen class is the UI for the registration screen."""
    
    def __init__(self, root, show_login_view):
        """The constructor of the RegistrationScreen class.
        
        Args:
            root (tk.Tk): The root of the UI.
        """
        
        self._root = root
        self._show_login_view = show_login_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._password_confirmation_entry = None
        
        self._init_screen()
        
    def pack(self):
        """Function to pack the UI."""
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        """Function to destroy the UI."""
        self._frame.destroy()

    def validate_registration(self):
        """Function to validate the user's registration credentials."""
        username = self._username_entry.get()
        password = self._password_entry.get()
        password_confirmation = self._password_confirmation_entry.get()
        
        if password == password_confirmation:
            # Hash the password
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            
            # Insert the user into database
            conn = create_connection("budget_tracker.db")
            add_user(conn, username, hashed_password)
            conn.close()
            
            # Destroy the registration screen and show the login screen
            self.destroy()
            self._show_login_view()
            
        else:
            # Display error message, if the passwords don't match
            error_label = customtkinter.CTkLabel(master=self._frame, text="Passwords do not match!", foreground="red")
            error_label.grid(padx=5, pady=5, sticky=constants.W)
            
    def _init_username_frame(self):
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = customtkinter.CTkEntry(master=self._frame)
        
        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)
        
    def _init_password_frame(self):
        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = customtkinter.CTkEntry(master=self._frame, show="*")
        
        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)
        
        password_confirmation_label = ttk.Label(master=self._frame, text="Confirm Password")
        self._password_confirmation_entry = customtkinter.CTkEntry(master=self._frame, show="*")
        
        password_confirmation_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_confirmation_entry.grid(padx=5, pady=5, sticky=constants.EW)
        
    def _init_screen(self):
        self._frame = ttk.Frame(master=self._root)
        
        self._init_username_frame()
        self._init_password_frame()
        
        
        register_button = customtkinter.CTkButton(master=self._frame, corner_radius=20, text="Register", command=self.validate_registration)
        register_button.grid(padx=5, pady=5, sticky=constants.EW)
        
        # Note to self, add command to the login button and functionality
        already_registered_button = customtkinter.CTkButton(master=self._frame, corner_radius=20, text="Already Registered? Sign in.", command=self._show_login_view)
        already_registered_button.grid(column=0, padx=5, pady=5, sticky=constants.EW)
        
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)