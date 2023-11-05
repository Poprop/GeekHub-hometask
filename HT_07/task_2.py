"""Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
   цифру;
   - якесь власне додаткове правило :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом."""


class FaultValidator(Exception):
    def __init__(self, message="You enter invalid login or password"):
        super().__init__(message)


def info_validation(login: str, password: str) -> bool:
    has_upper = any(el.isupper() for el in password)
    has_digit = any(el.isdigit() for el in password)
    if 3 <= len(login) <= 50 and len(password) >= 8 and has_digit and has_upper:
        return True
    else:
        raise FaultValidator()


try:
    login: str = input("Enter your login (from 3 to 50 symbols): ")
    password: str = input(
        "Enter your password (it must contain not less then 3 symbols , one digit and one upper letter: ")
    info_validation(login, password)
    print("Access is allowed")
except FaultValidator as e:
    print(e)
