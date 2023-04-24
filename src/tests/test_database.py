import unittest
import sqlite3
from database.database import create_connection, create_tables, add_user, hash_password, get_user, add_transaction, get_transactions, get_budget_summary, get_expense_summary, get_income_summary, delete_transaction


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.conn = create_connection(":memory:")
        create_tables(self.conn)

    def closeConnection(self):
        self.conn.close()

    def test_add_user(self):
        username = "test_user"
        password = hash_password("Password123!")
        result = add_user(self.conn, username, password)

        self.assertEqual(result, "Success")

        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT username, password FROM users WHERE username=?", (username,))
        user = cursor.fetchone()

        self.assertEqual(user[0], username)
        self.assertEqual(user[1], password)

    def test_add_existing_user(self):
        username = "test_user"
        password = hash_password("Password123!")
        add_user(self.conn, username, password)
        result = add_user(self.conn, username, password)

        self.assertEqual(result, "UserExists")

    def test_get_user(self):
        username = "test_user"
        password = hash_password("Password123!")
        add_user(self.conn, username, password)
        user = get_user(self.conn, username, password)

        self.assertIsNotNone(user)
        self.assertEqual(username, user[1])
        self.assertEqual(password, user[2])

    def test_add_transaction(self):
        username = "test_user"
        password = hash_password("Password123!")
        add_user(self.conn, username, password)
        user = get_user(self.conn, username, password)
        user_id = user[0]

        add_transaction(self.conn, user_id, "Income", 1000)
        add_transaction(self.conn, user_id, "Expense", 500)

        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM transactions WHERE user_id=?", (user_id,))
        transactions = cursor.fetchall()

        self.assertEqual(len(transactions), 2)

    def test_get_transactions(self):
        username = "test_user"
        password = hash_password("Password123!")
        add_user(self.conn, username, password)
        user = get_user(self.conn, username, password)
        user_id = user[0]

        add_transaction(self.conn, user_id, "Income", 1000)
        add_transaction(self.conn, user_id, "Expense", 500)

        transactions = get_transactions(self.conn, user_id)

        self.assertEqual(len(transactions), 2)

    def test_get_budget_summary(self):
        username = "test_user"
        password = hash_password("Password123!")
        add_user(self.conn, username, password)
        user = get_user(self.conn, username, password)
        user_id = user[0]

        add_transaction(self.conn, user_id, "Budget", 2000)

        budget_summary = get_budget_summary(self.conn, user_id)

        self.assertEqual(budget_summary, 2000)

    def test_get_expense_summary(self):
        username = "test_user"
        password = hash_password("Password123!")
        add_user(self.conn, username, password)
        user = get_user(self.conn, username, password)
        user_id = user[0]

        add_transaction(self.conn, user_id, "Expense", 500)

        expense_summary = get_expense_summary(self.conn, user_id)

        self.assertEqual(expense_summary, 500)

    def test_get_income_summary(self):
        username = "test_user"
        password = hash_password("Password123!")
        add_user(self.conn, username, password)
        user = get_user(self.conn, username, password)
        user_id = user[0]

        add_transaction(self.conn, user_id, "Income", 1000)

        income_summary = get_income_summary(self.conn, user_id)

        self.assertEqual(income_summary, 1000)

    def test_delete_transaction(self):
        # Initialize a temporary in-memory SQLite database for testing
        conn = sqlite3.connect(":memory:")

        # Create 'transactions' table in the database
        conn.execute('''CREATE TABLE transactions (
                            id INTEGER PRIMARY KEY,
                            user_id INTEGER,
                            type TEXT,
                            amount REAL,
                            date TEXT
                        )''')

        # Insert sample data into the 'transactions' table
        sample_transactions = [(1, "Budget", 1000, "2023-04-20"),
                               (2, "Expense", 200, "2023-04-21"),
                               (3, "Income", 300, "2023-04-22")]
        conn.executemany('''INSERT INTO transactions (user_id, type, amount, date)
                            VALUES (?, ?, ?, ?)''', sample_transactions)
        conn.commit()

        # Call the delete function with transaction_id 2
        delete_transaction(conn, 2)

        # Check if the transaction was successfully deleted
        cur = conn.cursor()
        cur.execute("SELECT * FROM transactions WHERE id=2")
        deleted_transaction = cur.fetchone()

        self.assertIsNone(deleted_transaction)
