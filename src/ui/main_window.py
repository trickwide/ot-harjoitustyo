from tkinter import ttk, constants, StringVar
import customtkinter
from database.database import create_connection, add_transaction, get_transactions, get_budget_summary, get_expense_summary, get_income_summary, delete_transaction


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
        """Function to initialize the dropdown menu."""

        choices = ["Budget", "Income", "Expense"]

        self._dropdown = customtkinter.CTkOptionMenu(
            master=self._frame, values=choices)
        self._dropdown.set(choices[0])
        self._dropdown.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_entry_field(self):
        """Function to initialize the entry field."""

        self._entry_value = StringVar()
        self._entry = customtkinter.CTkEntry(
            master=self._frame, placeholder_text="Input in format 10 or 10.00", textvariable=self._entry_value)
        self._entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_submit_button(self):
        """Function to initialize the submit button."""

        self._submit_button = customtkinter.CTkButton(
            master=self._frame, corner_radius=20, text="Submit", command=self.submit_value)
        self._submit_button.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_info_labels(self):
        """Function to initialize the info labels."""

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
        """Function to update the info labels."""

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
        """Function to delete a transaction and update the history and info labels after deletion."""
        # Delete the transaction from the database
        delete_transaction(self.conn, transaction_id)

        # Update the info labels and history section
        self._update_info_labels()
        self._init_history_section()

    def create_delete_button(self, master, transaction_id):
        """Function to create delete button for history section"""

        delete_button = customtkinter.CTkButton(
            master=master,
            corner_radius=20,
            text="Delete",
            command=lambda: self.delete_transaction(transaction_id)
        )
        return delete_button

    def _display_transaction(self, index, transaction_id, transaction_type, transaction_amount, transaction_date):
        """Function to display a transaction in the history section."""

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

        # "Delete" button for each transaction
        delete_button = self.create_delete_button(
            master=self._history_frame,
            transaction_id=transaction_id
        )
        delete_button.grid(column=4, row=index, padx=5, pady=5)

    def _init_history_section(self):
        """Function to initialize the history section."""

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

                # Display transaction information
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
        """Function to initialize the log out button."""

        self._log_out_button = customtkinter.CTkButton(
            master=self._frame, corner_radius=20, text="Log Out", command=self.log_out)
        self._log_out_button.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_screen(self):
        """Function to initialize the UI components of main window"""

        self._frame = ttk.Frame(master=self._root)
        self._init_dropdown()
        self._init_entry_field()
        self._init_submit_button()
        self._init_log_out_button()
        self._init_info_labels()
        self._init_history_section()

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
