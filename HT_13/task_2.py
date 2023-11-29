"""Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки (включіть фантазію).
Наприклад вона може містити класи Person, Teacher, Student, Book, Shelf, Author, Category і.т.д."""


class Person:
    def __int__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age} years old"


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def __str__(self):
        return f"{super().__str__} , Subject:{self.subject}"


class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def __str__(self):
        return f"{super().__str__()} study in {self.grade}"


class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = False

    def check_in(self):
        if not self.available:
            self.available = True
        else:
            print(f"{self.title} is already available")

    def check_out(self):
        if self.available:
            self.available = False
        else:
            print(f"{self.title} is already unavailable")


    def __str__(self):
        status = "Available" if self.available else "Not available"
        return f"Book: {self.title}\nwriten by: {self.author}\ngenre: {self.genre}\nstatus:{status}"


book = Book("Harry Potter", "Johan Rouling", "Fantasy")
print(book.check_in())
print(book.__str__())
