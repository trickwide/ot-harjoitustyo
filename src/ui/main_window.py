from tkinter import ttk, constants, StringVar
import customtkinter

class MainWindow:
    """The MainWindow class is the UI for the main window after successful login."""
    
    def __init__(self, root):
        """The constructor of the MainWindow class.

        Args:
            root (tk.Tk): The root of the UI.
        """
        self._root = root
        self._frame = None
        self._entry_value = None
        self._init_screen()
        
    def pack(self):
        """Function to pack the UI."""
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        """Function to destroy the UI."""
        self._frame.destroy()
        
    def submit_value(self):
        """Function to submit the value entered in the entry field."""
        pass

    def _init_dropdown(self):
        choices = ["Budget", "Income", "Expense"]
        dropdown = customtkinter.CTkOptionMenu(master=self._frame, values=choices)
        dropdown.set(choices[0])
        
        dropdown.grid(padx=5, pady=5, sticky=constants.EW)
        
        
    def _init_entry_field(self):
        self._entry_value = StringVar()
        entry = customtkinter.CTkEntry(master=self._frame, placeholder_text="Input in format 10 or 10.00")
        entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_submit_button(self):
        submit_button = customtkinter.CTkButton(master=self._frame, corner_radius=20, text="Submit", command=self.submit_value)
        submit_button.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_info_labels(self):
        pass  # TODO: Add labels to display the current Budget, Income, and Expense
    
    def _init_history_section(self):
        pass  # TODO: Add a section to display the history of inputs

    def _init_screen(self):
        self._frame = ttk.Frame(master=self._root)
        self._init_dropdown()
        self._init_entry_field()
        self._init_submit_button()
        self._init_info_labels()
        self._init_history_section()
        
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)