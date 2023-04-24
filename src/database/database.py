import os
import sqlite3
from sqlite3 import Error
import hashlib


def create_connection(db_file):
    """ Create a database connection to a SQLite database """
    conn = None
    try:
      # Construct an absolute path to the database file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, db_file)
        
        conn = sqlite3.connect(db_file)
    except Error as error:
        print(error)

    return conn


def create_tables(conn):
    """Create the required tables if they do not exist."""
    users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
    """

    transactions_table = """
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        );
    """

    try:
        cursor = conn.cursor()
        cursor.execute(users_table)
        cursor.execute(transactions_table)
    except Error as error:
        print(error)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def add_user(conn, username, password):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    if user:
        return "UserExists"

    cursor.execute("""
    INSERT INTO users (username, password) VALUES (?, ?)
    """, (username, password))
    conn.commit()
    return "Success"


def get_user(conn, username, password):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM users WHERE username=? AND password=?
    """, (username, password))
    return cursor.fetchone()


def add_transaction(conn, user_id, transaction_type, amount):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transactions (user_id, type, amount) VALUES (?, ?, ?)
    """, (user_id, transaction_type, amount))
    conn.commit()


def get_transactions(conn, user_id, limit=10):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM transactions WHERE user_id=? ORDER BY timestamp DESC LIMIT ?
    """, (user_id, limit))
    return cursor.fetchall()


def get_budget_summary(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT SUM(amount) FROM transactions WHERE user_id=? AND type=?
    """, (user_id, "Budget"))
    return cursor.fetchone()[0] or 0


def get_expense_summary(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT SUM(amount) FROM transactions WHERE user_id=? AND type=?
    """, (user_id, "Expense"))
    return cursor.fetchone()[0] or 0


def get_income_summary(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT SUM(amount) FROM transactions WHERE user_id=? AND type=?
    """, (user_id, "Income"))
    return cursor.fetchone()[0] or 0


def delete_transaction(conn, transaction_id):
    """Delete a transaction by transaction_id."""
    cur = conn.cursor()
    cur.execute("DELETE FROM transactions WHERE id=?", (transaction_id,))
    conn.commit()


def setup_database(db_file):
    conn = create_connection(db_file)
    if conn:
        create_tables(conn)
        conn.commit()


setup_database("budget_tracker.db")
