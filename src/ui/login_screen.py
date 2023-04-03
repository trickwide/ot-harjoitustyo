from tkinter import ttk, constants
import customtkinter
import hashlib
from database import create_connection, get_user

class LoginScreen:
    """The LoginScreen class is the UI for the login screen."""
    
    def __init__(self, root, show_registration_view, show_main_window):
        """The constructor of the LoginScreen class.
        
        Args:
            root (tk.Tk): The root of the UI.
        """
        self._root = root
        self._show_registration_view = show_registration_view
        self._show_main_window = show_main_window
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        
        self._init_screen()

    def pack(self):
        """Function to pack the UI."""
        self._frame.pack(fill=constants.X)
        
    def destroy(self):
        """Function to destroy the UI."""
        self._frame.destroy()

    def validate_login(self):
        """Function to validate the user's login credentials."""
        username = self._username_entry.get()
        password = self._password_entry.get()
        
        if username and password:
            # Hash the password
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            # Create a connection to the database
            conn = create_connection("budget_tracker.db")
            
            # Get the user from the database
            user = get_user(conn, username, password_hash)
            
            # If the user exists and password is correct, show the main window
            if user:
                self._show_main_window()
                self.destroy()
            else:
                # SHOW ERROR MESSAGE, needs to be added
                pass
    
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
    
    def _init_screen(self):
        self._frame = ttk.Frame(master=self._root)
        
        self._init_username_frame()
        self._init_password_frame()
        
        # Note to self, add command to the login button
        login_button =  customtkinter.CTkButton(master=self._frame, corner_radius=20, text="Login", command=self.validate_login)
        
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        
        login_button.grid(padx=5, pady=5, sticky=constants.EW)