from ui.login_screen import LoginScreen
from ui.registration_screen import RegistrationScreen
from ui.main_window import MainWindow


class UI:
    """The UI class is the main UI class."""

    def __init__(self, root):
        """The constructor of the UI class.

        Args:
            root: The root of the UI.
        """
        self._root = root
        self._current_view = None

    def start(self):
        """Function to start the UI."""
        self._show_registration_screen()

    def _hide_current_view(self):
        """Function to hide the current view"""

        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_screen(self):
        """Function to hide the current view and show the login screen."""

        self._hide_current_view()
        self._current_view = LoginScreen(
            self._root, self._show_registration_screen, self._show_main_window)
        self._current_view.pack()

    def _show_registration_screen(self):
        """Function to hide the current view and show the registration screen."""

        self._hide_current_view()
        self._current_view = RegistrationScreen(
            self._root, self._show_login_screen)
        self._current_view.pack()

    def _show_main_window(self, user_id):
        """Function to hide the current view and show the main window.

        Args:
            user_id: The id of the user.
        """

        self._hide_current_view()
        self._current_view = MainWindow(
            self._root, user_id, self._show_login_screen)
        self._current_view.pack()
