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
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_screen(self):
        self._hide_current_view()
        self._current_view = LoginScreen(self._root, self._show_registration_screen, self._show_main_window)
        self._current_view.pack()
    
    def _show_registration_screen(self):
        self._hide_current_view()
        self._current_view = RegistrationScreen(self._root, self._show_login_screen)
        self._current_view.pack()
        
    def _show_main_window(self):
        self._hide_current_view()
        self._current_view = MainWindow(self._root)
        self._current_view.pack()