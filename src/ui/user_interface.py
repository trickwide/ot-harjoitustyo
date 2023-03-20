from ui.login_screen import LoginScreen

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
        self._show_login_screen()
        
    def _show_login_screen(self):
        self._current_view = LoginScreen(self._root)
        self._current_view.pack()