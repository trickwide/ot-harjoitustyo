from tkinter import ttk, constants
import customtkinter
from validation.validation import validate_login


class LoginScreen:
    """The LoginScreen class is the UI for the login screen."""

    def __init__(self, root, show_registration_view, show_main_window):
        """The constructor of the LoginScreen class.

        Args:
            root (tk.Tk): The root of the UI.
            show_registration_view (function): The function to display the registration view.
            show_main_window (function): The function to display the main window.
        """
        self._root = root
        self._show_registration_view = show_registration_view
        self._show_main_window = show_main_window
        self.validate_login = validate_login
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_label = None

        self._init_screen()

    def pack(self):
        """Method to pack the UI."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Method to destroy the UI."""
        self._frame.destroy()

    def display_error_message(self, message):
        """
        Method to display an error message for a specified duration.

        Args:
            message (str): The error message to display.
        """

        if self._error_label:
            self._error_label.destroy()

        self._error_label = ttk.Label(
            master=self._frame, text=message, foreground="red")
        self._error_label.grid(padx=5, pady=5, sticky=constants.W)
        self._root.after(5000, self._error_label.destroy)

    def _validate_login(self, username, password, show_main_window, display_error_message, destroy):
        """
        Method to validate the user's login credentials and either display an error message or show the main window.

        Args:
            username (str): The username provided by the user.
            password (str): The password provided by the user.
            show_main_window (callable): A function to display the main window after successful login.
            display_error_message (callable): A function to display an error message when login credentials are invalid.
            destroy (callable): A function to destroy the login screen.
        """

        validate_login(username, password, show_main_window,
                       display_error_message, destroy)

    def _init_username_frame(self):
        """Method to initialize the username frame on the login screen."""

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = customtkinter.CTkEntry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_password_frame(self):
        """Method to initialize the password frame on the login screen."""

        password_label = ttk.Label(master=self._frame, text="Password")

        self._password_entry = customtkinter.CTkEntry(
            master=self._frame, show="*")

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_screen(self):
        """Method to initialize the login screen UI components."""

        self._frame = ttk.Frame(master=self._root)

        self._init_username_frame()
        self._init_password_frame()

        login_button = customtkinter.CTkButton(
            master=self._frame, corner_radius=20, text="Login", command=lambda: self._validate_login(
                self._username_entry.get(),
                self._password_entry.get(),
                self._show_main_window,
                lambda msg: self.display_error_message(msg),
                self.destroy))

        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        not_registered_button = customtkinter.CTkButton(
            master=self._frame, corner_radius=20, text="Not registered? Register here.", command=self._show_registration_view)
        not_registered_button.grid(
            column=0, padx=5, pady=5, sticky=constants.EW)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
