from tkinter import ttk, constants, StringVar, messagebox
from CTkMessagebox import CTkMessagebox
import customtkinter
from database.database import add_transaction, get_transactions, get_budget_summary, get_expense_summary, get_income_summary, delete_transaction, delete_account
from services.connection_services import get_db_connection


class MainWindow:
    """The MainWindow class is the UI for the main window after successful login."""

    def __init__(self, root, user_id, show_login_screen):
        """The constructor of the MainWindow class.

        Args:
            root (tk.Tk): The root of the UI.
            user_id (int): The user ID for the logged-in user.
            show_login_screen (function): A callback function to display the login screen.
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
        self.conn = get_db_connection()
        self._init_screen()
        self._update_info_labels()
        self._init_history_section()

    def pack(self):
        """Method to pack the UI."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Method to destroy the UI."""
        self._frame.destroy()

    def log_out(self):
        """Method to log out the user, close the main window and open login window."""
        self.destroy()
        self._show_login_screen()

    def submit_value(self):
        """Method to submit the value entered in the entry field."""
        try:
            value = float(self._entry_value.get())
            option = self._dropdown.get()

            add_transaction(self.conn, self.user_id, option, value)
            self._update_info_labels()
            self._init_history_section()
        except ValueError:
            pass

    def _init_dropdown(self):
        """Method to initialize the dropdown menu."""

        choices = ["Budget", "Income", "Expense"]

        self._dropdown = customtkinter.CTkOptionMenu(
            master=self._frame, values=choices)
        self._dropdown.set(choices[0])
        self._dropdown.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_entry_field(self):
        """Method to initialize the entry field."""

        self._entry_value = StringVar()
        self._entry = customtkinter.CTkEntry(
            master=self._frame, placeholder_text="Input in format 10 or 10.00", textvariable=self._entry_value)
        self._entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_submit_button(self):
        """Method to initialize the submit button."""

        self._submit_button = customtkinter.CTkButton(
            master=self._frame, corner_radius=20, text="Submit", command=self.submit_value)
        self._submit_button.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_info_labels(self):
        """Method to initialize the info labels."""

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
        """Method to update the info labels."""

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

    def delete_transaction(self, transaction_id):
        """
        Method to delete a transaction and update the history and info labels after deletion.

        Args:
            transaction_id (int): ID of the transaction.
        """

        delete_transaction(self.conn, transaction_id)

        self._update_info_labels()
        self._init_history_section()

    def create_delete_button(self, master, transaction_id):
        """
        Method to create delete button for history section.

        Args:
            master (tkinter.Frame): The frame in which the button will be placed.
            transaction_id (int): ID of the transaction.
        """

        delete_button = customtkinter.CTkButton(
            master=master,
            corner_radius=20,
            text="Delete",
            command=lambda: self.delete_transaction(transaction_id)
        )
        return delete_button

    def delete_account(self):
        """Method to delete the user account."""

        message = CTkMessagebox(
            title="Delete Account?", message="Are you sure you want to delete your account?", option_1="No", option_2="Yes")
        response = message.get()

        if response == "Yes":
            delete_account(self.conn, self.user_id)
            self.log_out()

    def _init_delete_account_button(self):
        """Method to initialize the delete account button."""

        self._delete_account_button = customtkinter.CTkButton(
            master=self._frame, corner_radius=20, text="Delete Account", command=self.delete_account)
        self._delete_account_button.grid(padx=5, pady=5, sticky=constants.EW)

    def _display_transaction(self, index, transaction_id, transaction_type, transaction_amount, transaction_date):
        """
        Method to display a transaction in the history section.

        Args: 
            index (int): Index of the transaction in the history section.
            transaction_id (int): ID of the transaction.
            transaction_type (str): Type of the transaction.
            transaction_amount (float): Amount of the transaction.
            transaction_date (str): Date of the transaction.
        """

        description_label = ttk.Label(
            master=self._history_frame,
            text=transaction_date
        )
        description_label.grid(column=0, row=index, padx=5, pady=5)

        amount_label = ttk.Label(
            master=self._history_frame,
            text=transaction_type
        )
        amount_label.grid(column=1, row=index, padx=5, pady=5)

        date_label = ttk.Label(
            master=self._history_frame,
            text=transaction_amount
        )
        date_label.grid(column=2, row=index, padx=5, pady=5)

        delete_button = self.create_delete_button(
            master=self._history_frame,
            transaction_id=transaction_id
        )
        delete_button.grid(column=4, row=index, padx=5, pady=5)

    def _init_history_section(self):
        """Method to initialize the history section."""

        if hasattr(self, "_history_frame"):
            self._history_frame.destroy()

        self._history_frame = customtkinter.CTkFrame(self._frame)

        transactions = get_transactions(self.conn, self.user_id)

        if transactions:
            for index, transaction in enumerate(transactions):
                transaction_id = transaction[0]
                transaction_type = transaction[2]
                transaction_amount = transaction[3]
                transaction_date = transaction[4]

                self._display_transaction(
                    index, transaction_id, transaction_type, transaction_amount, transaction_date)

        else:
            no_transactions_label = ttk.Label(
                master=self._history_frame,
                text="No transactions in the database."
            )
            no_transactions_label.grid(padx=5, pady=5)

        self._history_frame.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_log_out_button(self):
        """Method to initialize the log out button."""

        self._log_out_button = customtkinter.CTkButton(
            master=self._frame, corner_radius=20, text="Log Out", command=self.log_out)
        self._log_out_button.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_screen(self):
        """Method to initialize the UI components of main window"""

        self._frame = ttk.Frame(master=self._root)
        self._init_dropdown()
        self._init_entry_field()
        self._init_submit_button()
        self._init_log_out_button()
        self._init_delete_account_button()
        self._init_info_labels()
        self._init_history_section()

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
