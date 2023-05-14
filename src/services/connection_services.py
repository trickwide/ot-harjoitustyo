from database.database import create_connection


def get_db_connection():

    return create_connection("budget_tracker.db")
