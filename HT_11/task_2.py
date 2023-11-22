# Створити клас Person, в якому буде присутнім метод __init__ який буде приймати якісь аргументи,
# які зберігатиме в відповідні змінні.
# - Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
# - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession
# (його не має інсувати під час ініціалізації).

class Pearson:
    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name

    def show_age(self):
        return self.age

    def print_name(self):
        return self.name

    def show_all_information(self):
        return f"{self.name} is {self.age} years old"


vasia = Pearson("Vasia", 25)
ivan = Pearson("Vania", 20)
vasia.profession = "Surgeon"
ivan.profession = "QA manual"
print(vasia.show_all_information())
print(vasia.profession)
