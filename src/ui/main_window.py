from tkinter import ttk, constants, StringVar
import customtkinter
from database.database import create_connection, add_transaction, get_transactions, get_budget_summary, get_expense_summary, get_income_summary


class MainWindow:
    """The MainWindow class is the UI for the main window after successful login."""

    def __init__(self, root, user_id, show_login_screen):
        """The constructor of the MainWindow class.

        Args:
            root (tk.Tk): The root of the UI.
            user_id (int): The user ID for the logged-in user.
        """
        self._root = root
        self._frame = None
        self._entry_value = None
        self.initial_budget = 0.0
        self.current_budget = 0.0
        self.total_expense = 0.0
        self.total_income = 0.0
        self.user_id = user_id
        self._show_login_screen = show_login_screen
        self.conn = create_connection("budget_tracker.db")
        self._init_screen()
        self._update_info_labels()
        self._init_history_section()

    def pack(self):
        """Function to pack the UI."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Function to destroy the UI."""
        self._frame.destroy()

    def log_out(self):
        """Function to log out the user, close the main window and open login window."""
        self.destroy()
        self._show_login_screen()

    def submit_value(self):
        """Function to submit the value entered in the entry field."""
        try:
            value = float(self._entry_value.get())
            option = self._dropdown.get()

            add_transaction(self.conn, self.user_id, option, value)
            self._update_info_labels()
            self._init_history_section()
        except ValueError:
            pass

    def _init_dropdown(self):
        choices = ["Budget", "Income", "Expense"]

        self._dropdown = customtkinter.CTkOptionMenu(
            master=self._frame, values=choices)
        self._dropdown.set(choices[0])
        self._dropdown.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_entry_field(self):
        self._entry_value = StringVar()
        self._entry = customtkinter.CTkEntry(
            master=self._frame, placeholder_text="Input in format 10 or 10.00", textvariable=self._entry_value)
        self._entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_submit_button(self):
        self._submit_button = customtkinter.CTkButton(
            master=self._frame, corner_radius=20, text="Submit", command=self.submit_value)
        self._submit_button.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_info_labels(self):
        self._initial_budget_label = ttk.Label(
            self._frame, text=f"Initial Budget: {self.initial_budget:.2f}")
        self._current_budget_label = ttk.Label(
            self._frame, text=f"Current Budget: {self.current_budget:.2f}")
        self._total_expense_label = ttk.Label(
            self._frame, text=f"Total Expenses: {self.total_expense:.2f}")
        self._total_income_label = ttk.Label(
            self._frame, text=f"Total Income: {self.total_income:.2f}")

        self._initial_budget_label.grid(padx=5, pady=5, sticky=constants.W)
        self._current_budget_label.grid(padx=5, pady=5, sticky=constants.W)
        self._total_expense_label.grid(padx=5, pady=5, sticky=constants.W)
        self._total_income_label.grid(padx=5, pady=5, sticky=constants.W)

    def _update_info_labels(self):
        self.initial_budget = get_budget_summary(self.conn, self.user_id)
        self.total_expense = get_expense_summary(self.conn, self.user_id)
        self.total_income = get_income_summary(self.conn, self.user_id)

        self.current_budget = self.initial_budget + \
            self.total_income - self.total_expense

        self._initial_budget_label.config(
            text=f"Initial Budget: {self.initial_budget:.2f}")
        self._current_budget_label.config(
            text=f"Current Budget: {self.current_budget:.2f}")
        self._total_expense_label.config(
            text=f"Total Expenses: {self.total_expense:.2f}")
        self._total_income_label.config(
            text=f"Total Income: {self.total_income:.2f}")

    def _init_history_section(self):

        if hasattr(self, "_history_frame"):
            self._history_frame.destroy()

        self._history_frame = customtkinter.CTkFrame(self._frame)
        self.history = get_transactions(self.conn, self.user_id)
        for i, row in enumerate(self.history):
            transaction_type, amount, timestamp = row[2], row[3], row[4]
            label = ttk.Label(
                self._history_frame, text=f"{timestamp}: {transaction_type} - {amount:.2f}")
            label.grid(row=i, column=0, padx=5, pady=5, sticky=constants.W)

        self._history_frame.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_log_out_button(self):
        self._log_out_button = customtkinter.CTkButton(
            master=self._frame, corner_radius=20, text="Log Out", command=self.log_out)
        self._log_out_button.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_screen(self):
        self._frame = ttk.Frame(master=self._root)
        self._init_dropdown()
        self._init_entry_field()
        self._init_submit_button()
        self._init_log_out_button()
        self._init_info_labels()
        self._init_history_section()

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
