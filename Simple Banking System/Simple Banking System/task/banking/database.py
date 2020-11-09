import sqlite3


def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn


def create_table(conn):
    cur = conn.cursor()
    try:
        cur.execute(
            """
            CREATE TABLE card (
                id INTEGER,
                number TEXT,
                pin TEXT,
                balance INTEGER DEFAULT 0
            );
            """
        )
        conn.commit()
    except:
        pass


# Queries

add_account = "INSERT INTO card VALUES (NULL, card_number, PIN);"

valid_account = "SELECT * FROM card WHERE card_number = number AND PIN = pin"

query_balance = "SELECT balance FROM card WHERE number = 'card_number' AND pin = 'PIN'"
