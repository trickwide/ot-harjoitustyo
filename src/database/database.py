import os
import sqlite3
from sqlite3 import Error
import hashlib


def create_connection(db_file):
    """
    Function to create a database connection to a SQLite database.

    Args: 
        db_file (str): The name of the database file.

    Returns:
        conn (sqlite3.Connection): The connection object to the SQLite database.
    """

    conn = None
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, db_file)

        conn = sqlite3.connect(db_file)
    except Error as error:
        print(error)

    return conn


def create_tables(conn):
    """
    Function to create the required tables (users, transactions) if they do not exist.

    Args:
        conn (sqlite3.Connection): The connection object to the SQLite database.
    """

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
    """
    Function to hash the given password using SHA-256.

    Args:
        password (str): The password to hash.

    Returns:
        str: The hashed password.
    """

    return hashlib.sha256(password.encode()).hexdigest()


def add_user(conn, username, password):
    """
    Function to add a new user to the database.

    Args:
        conn (sqlite3.Connection): The connection object to the SQLite database.
        username (str): The username of the new user.
        password (str): The hashed password of the new user.

    Returns:
        str: "Success" if the user is added, "UserExists" if the user already exists.
    """

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
    """
    Function that retrieves a user from the database based on the given username and password.

    Args:
        conn (sqlite3.Connection): The connection object to the SQLite database.
        username (str): The username of the user.
        password (str): The hashed password of the user.

    Returns:
        tuple: The user information if found, None otherwise.
    """

    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM users WHERE username=? AND password=?
    """, (username, password))
    return cursor.fetchone()


def add_transaction(conn, user_id, transaction_type, amount):
    """
    Function to add a transaction to the database.

    Args:
        conn (sqlite3.Connection): The connection object to the SQLite database.
        user_id (int): The ID of the user who made the transaction.
        transaction_type (str): The type of transaction (e.g., "Budget", "Expense", "Income").
        amount (float): The amount of the transaction.
    """

    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transactions (user_id, type, amount) VALUES (?, ?, ?)
    """, (user_id, transaction_type, amount))
    conn.commit()


def get_transactions(conn, user_id, limit=10):
    """
    Function that retrieves the most recent transactions for a user, up to the specified limit.

    Args:
        conn (sqlite3.Connection): The connection object to the SQLite database.
        user_id (int): The ID of the user whose transactions to retrieve.
        limit (int): The maximum number of transactions to retrieve (default: 10).

    Returns:
        list: A list of tuples containing the transaction information.
    """

    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM transactions WHERE user_id=? ORDER BY timestamp DESC LIMIT ?
    """, (user_id, limit))
    return cursor.fetchall()


def get_budget_summary(conn, user_id):
    """
    Function that calculates the total budget for a user.

    Args:
        conn (sqlite3.Connection): The connection object to the SQLite database.
        user_id (int): The ID of the user whose budget to calculate.

    Returns:
        float: The total budget for the user.
    """

    cursor = conn.cursor()
    cursor.execute("""
        SELECT SUM(amount) FROM transactions WHERE user_id=? AND type=?
    """, (user_id, "Budget"))
    return cursor.fetchone()[0] or 0


def get_expense_summary(conn, user_id):
    """
    Function that calculates the total expenses for a user.

    Args:
        conn (sqlite3.Connection): The connection object to the SQLite database.
        user_id (int): The ID of the user whose expenses to calculate.

    Returns:
        float: The total expenses for the user.
    """

    cursor = conn.cursor()
    cursor.execute("""
        SELECT SUM(amount) FROM transactions WHERE user_id=? AND type=?
    """, (user_id, "Expense"))
    return cursor.fetchone()[0] or 0


def get_income_summary(conn, user_id):
    """
    Function that calculates the total income for a user.

    Args:
        conn (sqlite3.Connection): The connection object to the SQLite database.
        user_id (int): The ID of the user whose income to calculate.

    Returns:
        float: The total income for the user.
    """

    cursor = conn.cursor()
    cursor.execute("""
        SELECT SUM(amount) FROM transactions WHERE user_id=? AND type=?
    """, (user_id, "Income"))
    return cursor.fetchone()[0] or 0


def delete_transaction(conn, transaction_id):
    """
    Function to delete a transaction by transaction_id.

    Args:
        conn (sqlite3.Connection): The connection object to the SQLite database.
        transaction_id (int): The ID of the transaction to delete.
    """

    cur = conn.cursor()
    cur.execute("DELETE FROM transactions WHERE id=?", (transaction_id,))
    conn.commit()


def delete_account(conn, user_id):
    """
    Delete a user account and all transactions associated to that user from the database.

    Args:
        conn (sqlite3.Connection): The connection object to the SQLite database.
        user_id (int): The ID of the user.
    """
    cur = conn.cursor()
    cur.execute("DELETE FROM transactions WHERE user_id=?", (user_id,))
    cur.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()


def setup_database(db_file):
    """
    Function to setup the database.

    Args:
        db_file (str): The name of the database file.
    """
    conn = create_connection(db_file)
    if conn:
        create_tables(conn)
        conn.commit()


setup_database("budget_tracker.db")
