"""1. Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення у вигляді
кортежа: периметр квадрата, площа квадрата та його діагональ."""
import math


def square(side):
    perimetr = side * 4
    area = side ** 2
    diagonal = side * math.sqrt(2)
    return(perimetr,area,diagonal)

print(square(int(input("Enter the square side value:  "))))
