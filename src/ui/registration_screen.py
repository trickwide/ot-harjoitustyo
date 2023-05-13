from tkinter import ttk, constants
from CTkMessagebox import CTkMessagebox
import customtkinter
from services.user_services import UserService


class RegistrationScreen:
    """The RegistrationScreen class is the UI for the registration screen."""

    def __init__(self, root, show_login_view):
        """The constructor of the RegistrationScreen class.

        Args:
            root (tk.Tk): The root of the UI.
            show_login_view (function): The function to display the login view.
        """

        self._root = root
        self._show_login_view = show_login_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._password_confirmation_entry = None
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

        CTkMessagebox(title="Registration error",
                      message=message, icon="cancel")

    def validate_registration(self):
        """Method to validate the user's registration credentials."""

        username = self._username_entry.get()
        password = self._password_entry.get()
        password_confirmation = self._password_confirmation_entry.get()

        success, message = UserService.register_user(
            username, password, password_confirmation)

        if not success:
            self.display_error_message(message)
        else:
            self.destroy()
            self._show_login_view()

    def _init_username_frame(self):
        """Method to initialize the username frame on the registration screen."""

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = customtkinter.CTkEntry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_password_frame(self):
        """Method to initialize the password frame on the registration screen."""

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = customtkinter.CTkEntry(
            master=self._frame, show="*")

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

        password_confirmation_label = ttk.Label(
            master=self._frame, text="Confirm Password")
        self._password_confirmation_entry = customtkinter.CTkEntry(
            master=self._frame, show="*")

        password_confirmation_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_confirmation_entry.grid(
            padx=5, pady=5, sticky=constants.EW)

    def _init_screen(self):
        """Method to initialize the registration screen UI components."""

        self._frame = ttk.Frame(master=self._root)

        self._init_username_frame()
        self._init_password_frame()

        register_button = customtkinter.CTkButton(
            master=self._frame, corner_radius=20, text="Register", command=self.validate_registration)
        register_button.grid(padx=5, pady=5, sticky=constants.EW)

        already_registered_button = customtkinter.CTkButton(
            master=self._frame, corner_radius=20, text="Already Registered? Sign in.", command=self._show_login_view)
        already_registered_button.grid(
            column=0, padx=5, pady=5, sticky=constants.EW)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
