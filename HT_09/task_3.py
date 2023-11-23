"""Програма-банкомат.
   Використувуючи функції створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.CSV>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.TXT>)
та історію транзакцій (файл <{username_transactions.JSON>);
      - є можливість як вносити гроші, так і знімати їх.
Обов'язкова перевірка введених даних (введено цифри; знімається не більше, ніж є на рахунку і т.д.).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. Але якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - на початку роботи - логін користувача (програма запитує ім'я/пароль). Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :))
      - потім - елементарне меню типн:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив, можете розширювати функціонал, але основне завдання має бути повністю реалізоване :)
    P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt, json відповідно)
    P.S.S. Добре продумайте структуру програми та функцій (edited) """
import csv
import os.path
import json

path_4_files = os.path.join(os.getcwd(), 'task_3_files')
if not os.path.exists(path_4_files):
    os.makedirs(path_4_files)
os.chdir(path_4_files)
users = [["Name", "Password"],
         ["Oleg", "5623"],
         ["Ilona", "6213"],
         ["Vasia", "5555"],
         ["Dmytro", "2452"]]
start_balance_info = [("Oleg", 25000),
                      ("Ilona", 5000),
                      ("Vasia", 50000),
                      ("Dmytro", 10000)]
file_csv_name = "Names&passwords.csv"
with open(file_csv_name, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(users)
for user, balance in start_balance_info:
    with open(f"{user}_balance.txt", "w", encoding="utf-8") as balance_txt:
        balance_txt.write(str(balance))
jason_info = {"User_name": None,
              "Transaction_purpose": None,
              "Amount": None,
              "Account balance": None}
with open("transaction.json", "w", encoding="utf-8") as json_file:
    json.dump(jason_info, json_file, indent=4)


class ATM:
    def __init__(self, balance_path, user_info_path, transaction_path):
        self.users = self.load_users(user_info_path)
        self.balance = self.load_balances(balance_path)
        self.transaction = self.load_transaction(transaction_path)
        self.current_user = None

    def load_transaction(self, transactions_path):
        with open(transactions_path, "r", encoding="utf-8") as transaction_json_file:
            return json.load(transaction_json_file)

    def save_changes(self, balances_path, users_file, transactions_file):
        #
        with open(users_file, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows([[user, password] for user, password in self.users.items()])

        for user, balance in self.balance.items():
            with open(os.path.join(balances_path, f"{user}_balance.txt"), 'w', encoding='utf-8') as balance_file:
                balance_file.write(str(balance))
        with open(transactions_file, 'w', encoding='utf-8') as json_file:
            json.dump(self.transaction, json_file, indent=4)

    def update_transaction(self, user, transaction_purpose, amount, balance):
        self.transaction["User_name"] = user
        self.transaction["Transaction_purpose"] = transaction_purpose
        self.transaction["Amount"] = amount
        self.transaction["Account balance"] = balance

    def load_users(self, user_info_path):
        with open(user_info_path, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file)
            users_data = {row[0]: row[1] for row in csv_reader}
        return users_data

    def load_balances(self, user_balance_path):
        balances = {}
        for user_balance_file in os.listdir(user_balance_path):
            if user_balance_file.endswith("_balance.txt"):
                user = user_balance_file.split("_")[0]
                with open(os.path.join(user_balance_path, user + "_balance.txt"), "r+",
                          encoding="utf-8") as balance_txt_file:
                    balance = int(balance_txt_file.read())
                    balances[user] = balance
        return balances

    def login(self, account_login: str, account_password: str):
        if account_login in self.users and self.users[account_login] == account_password:
            self.current_user = account_login
            print(f"Congratulations you have entered to the system as {account_login}")
        else:
            print("Your enter invalid login or password")

    def logout(self, account_name):
        self.current_user = None
        print("You have logged out from the system")

    def start(self):
        while True:
            choice = input("1 - Use ATM\n"
                           "2 - Exit\n"
                           "Enter your action: ")

            if choice == "1":

                user_name_function = input("enter your login: ").strip().capitalize()
                password = input("enter your password: ")
                self.login(user_name_function, password)
                if self.current_user:
                    self.menu(user_name_function)
                    break
            if choice == "2":
                print("Good bye , see    you next time")
                break
            else:
                print("Your choice is incorrect , you should enter 1 (for using ATM) or 2 ( for exit)")

    def menu(self, user_name_function):
        user = user_name_function
        while self.current_user:
            menu_options = {
                '1': 'check_balance',
                '2': 'deposit',
                '3': 'withdraw',
                '4': 'logout'
            }
            print(f"ATM menu , choose one of this action by entering number: ")
            for key, value in menu_options.items():
                print(f"{key} <-------- {value}")
            choice = input("Your choice is : ")
            if choice in menu_options:
                getattr(self, menu_options[choice])(account_name=user)
            else:
                print("Invalid option , try again")
            if not self.current_user:
                break

    def add_account(self, users_name: str, user_password: str):
        if users_name not in self.users:
            self.users[users_name] = [user_password]
            self.balance[users_name] = 0
            print(f"Created new account for {users_name} it balance is 0")
        else:
            print(f"Account {users_name} already exists")

    def check_balance(self, account_name: str):
        if account_name in self.balance:
            print(f"Your balance is {self.balance[account_name]}")
        else:
            print(f"Account {account_name} not exists")

    def deposit(self, account_name: str):
        if account_name in self.balance:
            amount = int(input("Enter please amount of deposit: "))
            self.balance[account_name] += amount
            print(f"On account {account_name} was successfully deposited {amount} UAH ,\n"
                  f"curent deposite is {self.balance[account_name]}")
            self.update_transaction(user=account_name, transaction_purpose="Deposit", amount=amount, balance=balance)
            self.save_changes(user_balance_path, users_info_path, users_transactions_path)
        else:
            print(f"Account {account_name} is not exists")

    def withdraw(self, account_name: str):
        if account_name in self.balance:
            amount = int(input("Enter amount of withdraw: "))
            if self.balance[account_name] >= amount:
                self.balance[account_name] -= amount
                print(f"From account {account_name} was successfully withrawed {amount} UAH ,\n"
                      f"current deposit is {self.balance[account_name]}")
                self.update_transaction(user=account_name, transaction_purpose="Withdraw", amount=amount,
                                        balance=balance)
                self.save_changes(user_balance_path, users_info_path, users_transactions_path)

            else:
                print(f"There is not enough money on your balance")


users_info_path = os.path.join(path_4_files, 'Names&passwords.csv')
user_balance_path = os.path.join(path_4_files, )
users_transactions_path = os.path.join(path_4_files, "transaction.json")
atm = ATM(user_balance_path, users_info_path, users_transactions_path)
atm.start()
