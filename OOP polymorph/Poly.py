
# """Базовий приклад з операторами """
# num1 = 1
# num2 = 2
# print(num1 + num2)
#
# str1 = "Python"
# str2 = "Programming"
# print(str1 + " " + str2)

# """Базовий приклад з функціями і їх варіацією поліморфізму"""
# print(len("Programiz"))
# print(len(["Python", "Java", "C"]))
# print(len({"Name": "John", "Address": "Nepal"}))
"""Приклад з класами та їх варіація поліморфізму у викоритсанні методів """
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
def print_area(shape):
    return shape.area()
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(print_area(circle))     # Output: 78.5
print(print_area(rectangle))