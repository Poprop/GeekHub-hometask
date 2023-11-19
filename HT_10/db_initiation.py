import os
import sqlite3

users = [["Admin", "admin"],
         ["Oleg", "5623"],
         ["Ilona", "6213"],
         ["Vasia", "5555"],
         ["Dmytro", "2452"]]
start_balance_info = [("Oleg", 25000),
                      ("Ilona", 5000),
                      ("Vasia", 50000),
                      ("Dmytro", 10000)]
initial_bill_inventory = [10, 20, 50, 100, 200, 500, 1000]
db_path = os.path.join(os.getcwd(), 'atm_database.db')
conn = sqlite3.connect(db_path)


def create_tables(*args, **kwargs):
    with conn:
        cur = conn.cursor()

        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
        users_table_exists = cur.fetchone() is not None

        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='balances';")
        balances_table_exists = cur.fetchone() is not None

        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='bills_inventory';")
        bills_inventory_table_exists = cur.fetchone() is not None

        if not users_table_exists or not balances_table_exists or not bills_inventory_table_exists:

            cur.execute("""CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    password TEXT NOT NULL)""")
            cur.execute("""CREATE TABLE IF NOT EXISTS balances (
                    users_id INTEGER PRIMARY KEY,
                    balance INTEGER DEFAULT 0 , 
                    FOREIGN KEY (users_id) REFERENCES users (id)
                    )""")
            cur.execute("""CREATE TABLE IF NOT EXISTS transactions(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    transaction_purpose TEXT,
                    amount INTEGER,
                    balance_after_transaction INTEGER,
                    FOREIGN KEY (user_id) REFERENCES users (id) 
                    )""")
            cur.execute("""CREATE TABLE IF NOT EXISTS bills_inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nominal INTEGER NOT NULL,
                quantity INTEGER DEFAULT 0
            )""")

            cur.executemany("""
                INSERT OR IGNORE INTO users (name , password ) VALUES (?,?)
            """, users)

            cur.executemany("""
                INSERT OR IGNORE INTO balances (users_id, balance) VALUES (?, ?)
            """, [(user_id + 1, balance) for user_id, balance in
                  enumerate([balance for _, balance in start_balance_info], start=1) if
                  users[user_id][0] != "Admin"])

            cur.executemany("""
                INSERT OR IGNORE INTO bills_inventory (nominal, quantity) VALUES (?, 0)
            """, [(nominal,) for nominal in initial_bill_inventory])

            print("Tables created.")
        else:
            pass



