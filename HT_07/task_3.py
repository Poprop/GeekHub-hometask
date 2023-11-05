"""На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - ' \
                                  'як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для
кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)"""


class RandomException(Exception):
    pass


def validator_func(login: str, password: str):
    if not login or not password:
        raise RandomException("You forgot enter login or password")
    if not any(el.isupper() for el in password):
        raise RandomException("Your password must contain at least one upper letter")
    if not any(el.isdigit() for el in password):
        raise RandomException("Your password must contain at least one digit")
    if not (3 <= len(login) <= 50):
        raise RandomException("Your login bigger than 50 or smaller than 3 symbols")
    if len(password) < 8:
        raise RandomException("Your password smaller then 8 symbols")
    return "OK , access is allowed"


def user_check(users: list) -> list:
    results = []
    for user in users:
        try:
            login, password, result = user[0], user[1], validator_func(user[0], user[1])
            results.append((login, password, result))
        except RandomException as e:
            results.append((user[0], user[1], str(e)))
    return results


if __name__ == '__main__':
    users_info_collection: list = [
        ('JohnDou', '43543f3f'),
        ('MiguelOhara', 'rew3234Rigj'),
        ('Milez', '13rw4488888'),
        ('Crowler', 'Fkeqwe343'),
        ('Spot', '35325432fewfw')
    ]
    validation_res = user_check(users_info_collection)
    for login, password, result in validation_res:
        print(f"Name: {login}\nPassword: {password}\nStratus: {result}\n________________")
