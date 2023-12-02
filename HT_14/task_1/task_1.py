"""Банкомат 3.0
- реалізуйте видачу купюр за логікою видавання найменшої кількості купюр.
Наприклад: 2560 --> 2х1000, 1х500, 3х20. Будьте обережні з "жадібним алгоритмом"!"""
import os
import sqlite3

import HT_14.task_1.curentexchange
from db_initiation import create_tables
from admin_panel import AdminATM
from random import randint
from collections import Counter
from HT_14.task_1.curentexchange import currently_exchange_rate


class ATM:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.current_user = None
        self.admin_atm = AdminATM(db_path)
        self.bill_inventory = {10: 0, 20: 0, 50: 0, 100: 0, 200: 0, 500: 0, 1000: 0}
        self.denominations = [1000, 500, 200, 100, 50, 20, 10]
        create_tables()

    def login(self, account_name: str, account_password: str):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("""SELECT id, name FROM users WHERE name=? AND password=?""", (account_name, account_password))
            result = cur.fetchone()
            if result:
                if len(result) == 2:
                    user_id, user_name = result
                    if user_name == "Admin":
                        self.admin_atm.admin_login(account_name, account_password)
                    else:
                        self.current_user = user_id
                        print(f"Congratulations you have entered to the system as {account_name}")
                else:
                    print("Unexpected result format from the database")
            else:
                print("Your enter invalid login or password")

    def logout(self):
        self.current_user = None
        print("You have logged out from the system")

    def start(self):
        while True:
            choice = input("1 - Use ATM\n"
                           "2 - Exit\n"
                           "3 - New account registration\n"
                           "Enter your action: ")

            if choice == "1":
                user_name_function = input("Enter your login: ").strip().capitalize()
                password = input("Enter your password: ").strip()
                self.login(user_name_function, password)
                if self.current_user:
                    self.menu(user_name_function)
                    break
            elif choice == "2":
                print("Good bye, see you next time")
                break
            elif choice == "3":
                print("Let's start creating a new account")
                self.add_account()
            else:
                print("Your choice is incorrect. Please enter 1 (for using ATM) or 2 (for exit)")

    def menu(self, user_name_function):
        user = user_name_function
        while self.current_user:
            menu_options = {
                '1': 'check_balance',
                '2': 'deposit',
                '3': 'withdraw',
                '4': 'logout',
                '5': 'currency_exchange'
            }
            print(f"ATM menu, choose one of these actions by entering a number: ")
            for key, value in menu_options.items():
                print(f"{key} <-------- {value}")
            choice = input("Your choice is: ")
            if choice in menu_options:
                getattr(self, menu_options[choice])()
            else:
                print("Invalid option, try again")
            if not self.current_user:
                break

    def currency_exchange(self):
        print("Available currency is : UAH , USD , EUR , PLN\nPlease enter bellow what currency you interested in")
        available = ["UAH", "USD", "EUR", "PLN"]
        what_you_have = None
        what_want_buy = None
        while what_you_have is None:
            try:
                what_you_have: str = (input("What currency do you have: ")).upper()
                if what_you_have not in available:
                    what_you_have = None
                    raise ValueError('You can use only available currency: ')
            except Exception as e:
                print(e)
        while what_want_buy is None:
            try:
                what_want_buy: str = (input("What currency you want to buy: ")).upper()
                if what_want_buy not in available:
                    what_want_buy = None
                    raise ValueError('You can use only available currency')
            except Exception as e:
                print(e)
        print(currently_exchange_rate(target_currency=what_you_have, base_currency=what_want_buy))

    def add_account(self):
        print("You enter the new account menu, please enter information for registration")

        def login_creation():
            while True:
                new_acc_inp = input("Enter your login: ").strip().capitalize()
                if not new_acc_inp.isalpha():
                    print("Your login can contain only alphabet letters, try again")
                else:
                    print("Everything is ok, choose your password")
                    return new_acc_inp

        def password_creation():
            while True:
                new_pas_inp = input("Enter your password, it should contain 4 numbers (0-9): ")
                if not new_pas_inp.isdigit() and len(new_pas_inp) != 4:
                    print("Your password contains letters or its length is more than 4 elements")
                else:
                    print("Everything is ok, now you can use your new account")
                    return new_pas_inp

        new_acc_login = login_creation()
        new_acc_password = password_creation()
        print("You enter the new account menu, please enter information for registration")
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("INSERT OR REPLACE INTO users (name, password,is_new) VALUES (?, ?, ?)",
                        (new_acc_login, new_acc_password, 0))
            self.conn.commit()
            cur.execute("""INSERT OR REPLACE INTO balances (users_id,balance) VALUES (?,?)""",
                        (cur.lastrowid, 0))
            self.conn.commit()
            print(
                f"Created a new account for {new_acc_login}. Its balance is 0.\nNow you can deposit some money to your "
                f"account using the Deposit menu after login")

            self.start()

    def save_transaction(self, user_id, transaction_purpose, amount, balance_after_transaction):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO transactions (user_id, transaction_purpose, amount, balance_after_transaction)
                VALUES (?, ?, ?, ?)
            """, (user_id, transaction_purpose, amount, balance_after_transaction))
            self.conn.commit()

    def check_balance(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT balance FROM balances WHERE users_id=?", (self.current_user,))
            result = cur.fetchone()
            if result:
                balance = result[0]
                print(f"Your balance is {balance}")
                return balance
            else:
                print("User not found or other appropriate message")

    def deposit(self):
        amount = 0
        with self.conn:
            while amount <= 0:
                amount = get_integer_input("Enter the amount of deposit: ")
                if amount < 0:
                    print("Enter number greater than 0")

            change = None
            if amount % 10 != 0:
                change = amount % 10
                amount = amount - change
            cur = self.conn.cursor()
            if self.is_new() == True:
                random = randint(1, 100)
                if random <= 10:
                    bonus = amount / 10
                    amount += bonus
                    cur.execute("UPDATE balances SET balance = balance + ? WHERE users_id = ?",
                                (amount, self.current_user))
                    print(f"Congratulation you have 10% bonus {bonus} UAH to your deposit as a new user!!!".upper())
                else:
                    cur.execute("UPDATE balances SET balance = balance + ? WHERE users_id = ?",
                                (amount, self.current_user))
            else:
                cur.execute("UPDATE balances SET balance = balance + ? WHERE users_id = ?",
                            (amount, self.current_user))
            self.conn.commit()
            print(f"On account, you have successfully deposited {amount} UAH.Your change is {change} UAH")
            self.check_balance()
            self.save_transaction(self.current_user, 'Deposit', amount, self.check_balance())
            # self.admin_atm.update_bill_inventory(amount)

    def is_new(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT is_new FROM users WHERE id = ? ", (self.current_user,))
            result = cur.fetchone()
            if result[0] == 0:
                cur.execute("UPDATE users SET is_new = 1  WHERE id = ?", (self.current_user,))
                return True
            else:
                return False

    # def withdraw(self):
    #     with self.conn:
    #         try:
    #             amount = get_integer_input("Enter the amount of withdrawal: ")
    #         except ValueError:
    #             print("Invalid input. Please enter a valid number.")
    #             return
    # 
    #         cur = self.conn.cursor()
    #         cur.execute("SELECT balance FROM balances WHERE users_id = ?", (self.current_user,))
    #         result = cur.fetchone()
    # 
    #         if result is not None and result[0] >= amount:
    #             if amount <= self.admin_atm.check_total_bank_for_user_funks():
    #                 if amount % 10 != 0:
    #                     print(
    #                         f"Sorry but there is no opportunity to give you {amount - (amount % 10)} in cash due to \n"
    #                         f"ATM can give a minimal nominal - 10 UAH")
    #                 amount = amount - (amount % 10)
    # 
    #                 combinations = self.generate_combinations(amount, self.denominations,
    #                                                           self.check_denominations())
    #                 best_combination = self.best_combination(combinations)
    # 
    #                 if best_combination is not None and best_combination:
    #                     print(best_combination)
    #                     for denomination, count in best_combination.items():
    #                         cur.execute("""UPDATE bills_inventory SET quantity = quantity - ? WHERE nominal = ?""",
    #                                     (count, denomination))
    # 
    #                     cur.execute("UPDATE balances SET balance = balance - ? WHERE users_id = ?",
    #                                 (amount, self.current_user))
    # 
    #                     print(f"From your account, {amount} UAH was successfully withdrawn. Your bills:")
    #                     for denomination, count in best_combination.items():
    #                         print(f"{denomination} x {count}")
    # 
    #                     self.save_transaction(self.current_user, 'Withdrawal', amount, self.check_balance())
    #                 else:
    #                     print("Insufficient funds in the ATM.")
    # 
    #             else:
    #                 print("There is not enough money in the ATM")
    #         else:
    #             print("There is not enough money in your balance")
    def withdraw(self):
        with self.conn:
            try:
                amount = get_integer_input("Enter the amount of withdrawal: ")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                return

            cur = self.conn.cursor()
            cur.execute("SELECT balance FROM balances WHERE users_id = ?", (self.current_user,))
            result = cur.fetchone()

            if result is not None and result[0] >= amount:
                if amount <= self.admin_atm.check_total_bank_for_user_funks():
                    if amount % 10 != 0:
                        print(
                            f"Sorry but there is no opportunity to give you {amount - (amount % 10)} in cash due to \n"
                            f"ATM can give a minimal nominal - 10 UAH")
                    amount = amount - (amount % 10)
                    greedy = self.greedy_update_bill_inventory(amount)
                    cur.execute("UPDATE balances SET balance = balance - ? WHERE users_id = ?",
                                (amount, self.current_user))
                    if greedy is not None and greedy:
                        print(greedy)
                        self.save_transaction(self.current_user, 'Withdrawal', amount, self.check_balance())

                    else:
                        print("Need some more time for trying make withdraw in another way...")

                        combinations = self.generate_combinations(amount, self.denominations,
                                                                  self.check_denominations())
                        best_combination = self.best_combination(combinations)

                        if best_combination:

                            for denomination, count in best_combination.items():
                                cur.execute("""UPDATE bills_inventory SET quantity = quantity - ? WHERE nominal = ?""",
                                            (count, denomination))

                            cur.execute("UPDATE balances SET balance = balance - ? WHERE users_id = ?",
                                        (amount, self.current_user))

                            print(f"From your account, {amount} UAH was successfully withdrawn. Your bills:")
                            for denomination, count in best_combination.items():
                                print(f"{denomination} x {count}")

                            self.save_transaction(self.current_user, 'Withdrawal', amount, self.check_balance())
                        else:
                            print("Insufficient funds in the ATM.")

                else:
                    print("There is not enough money in the ATM")
            else:
                print("There is not enough money in your balance")

    def check_denominations(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("""SELECT * FROM bills_inventory""")
            rows = cur.fetchall()
            res = {row[1]: row[2] for row in rows}
            return res

    def generate_combinations(self, amount: int, denomination: list, den_quantity: dict,
                              current_combination=None) -> list:
        # print(f"amount - {amount} , denom - {denomination} , den_quant - {den_quantity}")
        if current_combination is None:
            current_combination = []
        if amount == 0:
            return [current_combination]

        combinations = []
        for i, denom in enumerate(denomination):
            if amount >= denom and den_quantity.get(denom, 0) > 0:
                remaining_denominations = denomination[i:]
                new_limits = den_quantity.copy()
                new_limits[denom] -= 1
                combinations += self.generate_combinations(amount - denom, remaining_denominations, new_limits,
                                                           current_combination + [denom])

        return combinations

    def greedy_update_bill_inventory(self, amount: int):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("""SELECT * FROM bills_inventory""")
            rows = cur.fetchall()
            current_inventory = {row[1]: row[2] for row in rows}
            withdrawn_bills = Counter()
            income_amount = amount

            for bill in sorted(current_inventory.keys(), reverse=True):
                while amount >= bill and current_inventory[bill] > 0:
                    current_inventory[bill] -= 1
                    amount -= bill
                    withdrawn_bills[bill] += 1
            if amount == 0:
                update_values = [(current_inventory[bill], bill) for bill in
                                 sorted(current_inventory.keys(), reverse=True)]
                print(f"From your account, {income_amount} UAH was successfully withdrawn. Your bills:")
                for bill, quant in withdrawn_bills.items():
                    print(f"{bill} x {quant}")
                for value in update_values:
                    cur.execute("""
                        UPDATE bills_inventory
                        SET quantity = ?
                        WHERE nominal = ?
                    """, value)
                return True

            else:
                print("There are no possibility to withdraw necessary value by greedy algorythm")
                return False

    def best_combination(self, combinations: list) -> dict:
        if len(combinations) == 0:
            return {}
        best = combinations[0]
        for combination in combinations:
            if len(combination) < len(best):
                best = combination
        return {note: best.count(note) for note in set(best)}


def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    db_path = os.path.join(os.getcwd(), 'atm_database.db')
    atm = ATM(db_path)
    atm.start()
