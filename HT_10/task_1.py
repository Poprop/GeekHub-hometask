"""Банкомат 2.0
    - усі дані зберігаються тільки в sqlite3 базі даних. Більше ніяких файлів. Якщо в попередньому завданні ви добре
    продумали структуру програми то у вас не виникне проблем швидко адаптувати її до нових вимог.
    - на старті додати можливість залогінитися або створити новго користувача (при створенні новго користувача,
    перевіряється відповідність логіну і паролю мінімальним вимогам. Для перевірки створіть окремі функції)
    - в таблиці (базі) з користувачами має бути створений унікальний користувач-інкасатор, який матиме розширені
    можливості (домовимось, що логін/пароль будуть admin/admin щоб нам було простіше перевіряти)
    - банкомат має власний баланс
    - кількість купюр в банкоматі обмежена. Номінали купюр - 10, 20, 50, 100, 200, 500, 1000
    - змінювати вручну кількість купюр або подивитися їх залишок в банкоматі може лише інкасатор
    - користувач через банкомат може покласти на рахунок лише сумму кратну мінімальному номіналу що підтримує банкомат.
    В іншому випадку - повернути "здачу" (наприклад при поклажі 1005 --> повернути 5). Але це не має впливати на
    баланс/кількість купюр банкомату, лише збільшуєтсья баланс користувача (моделюємо наявність двох незалежних касет
    в банкоматі - одна на прийом, інша на видачу)
    - зняти можна лише в межах власного балансу, але не більше ніж є всього в банкоматі.
    - при неможливості виконання якоїсь операції - вивести повідомлення з причиною (не вірний логін/пароль, недостатньо
    коштів на раунку, неможливо видати суму наявними купюрами тощо.) """
import os
import sqlite3
from db_initiation import create_tables
from admin_panel import AdminATM


class ATM:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.current_user = None
        self.admin_atm = AdminATM(db_path)

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
                '4': 'logout'
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

    def add_account(self):
        print("You enter the new account menu, please enter information for registration")

        def login_creation():
            while True:
                new_acc_inp = input("Enter your login: ").strip()
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
            cur.execute("INSERT OR REPLACE INTO users (name, password) VALUES (?, ?)",
                        (new_acc_login, new_acc_password))
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
        with self.conn:
            amount = get_integer_input("Enter the amount of deposit: ")
            change = None
            if amount % 10 != 0:
                change = amount % 10
                amount = amount - change
            cur = self.conn.cursor()
            cur.execute("UPDATE balances SET balance = balance + ? WHERE users_id = ?", (amount, self.current_user))
            self.conn.commit()
            print(f"On account, you have successfully deposited {amount} UAH.Your change is {change} UAH")
            self.check_balance()
            self.save_transaction(self.current_user, 'Deposit', amount, self.check_balance())
            self.admin_atm.update_bill_inventory(amount)

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

                    cur.execute("UPDATE balances SET balance = balance - ? WHERE users_id = ?",
                                (amount, self.current_user))
                    self.conn.commit()
                    print(f"From your account, {amount} UAH was successfully withdrawn.")
                    self.save_transaction(self.current_user, 'Withdrawal', amount, self.check_balance())
                    self.admin_atm.update_bill_inventory(-amount)
                else:
                    print("There is not enough money in the ATM")
            else:
                print("There is not enough money in your balance")


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
