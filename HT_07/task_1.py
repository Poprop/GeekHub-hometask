# Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
# Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий
# параметр <silent> (значення за замовчуванням - <False>).
# Логіка наступна:
#     якщо введено коректну пару ім'я/пароль - вертається True;
#     якщо введено неправильну пару ім'я/пароль:
#     якщо silent == True - функція вертає False
#     якщо silent == False -породжується виключення LoginException (його також треба створити =))

class LoginException(Exception):
    def __init__(self, message="Your password or login was incorrect"):
        super().__init__(message)


def Passwordcheck(username: str, password: str, silent: bool = False):
    if not username or not password:
        return False
    user_list = [{'username': "Sokoliuk", "password": "3234fweddad"},
                 {'username': "Pastushenko", "password": "qvasdd3442"},
                 {'username': "Masiuk", "password": "12345ad"},
                 {'username': "Nyzovyi", "password": "!dqdqwd4"},
                 {'username': "Dic", "password": "reww432d"},
                 {'username': "Lytovchenko", "password": "gerew421"}, ]
    for users in user_list:
        if users["username"] == username and users["password"] == password:
            return True
    if not silent:
        raise LoginException()
    return False


if __name__ == "__main__":
    try:
        login: str = input("Please enter your Login : ")
        parol: str = input("Please enter your Password : ")
        print(Passwordcheck(username=login, password=parol))
    except LoginException as e:
        print(e)
