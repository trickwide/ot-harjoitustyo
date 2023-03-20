from tkinter import ttk, StringVar, constants

class LoginScreen:
    """The LoginScreen class is the UI for the login screen."""
    
    def __init__(self, root):
        """The constructor of the LoginScreen class.
        
        Args:
            root (tk.Tk): The root of the UI.
        """
        self._root = root
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        
        self._init_screen()

    def pack(self):
        """Function to pack the UI."""
        self._frame.pack(fill=constants.X)

    def validate_login():
        """Function to validate the user's login credentials."""
        pass
    
    def _init_username_frame(self):
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)
        
        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)
        
    
    def _init_password_frame(self):
        password_label = ttk.Label(master=self._frame, text="Password")

        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)
    
    def _init_screen(self):
        self._frame = ttk.Frame(master=self._root)
        
        self._init_username_frame()
        self._init_password_frame()
        
        # Note to self, add command to the login button
        login_button = ttk.Button(master=self._frame, text="Login")
        
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        
        login_button.grid(padx=5, pady=5, sticky=constants.EW)