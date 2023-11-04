"""1. Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення у вигляді
кортежа: периметр квадрата, площа квадрата та його діагональ."""
import math


def square(side) -> int:
    perimetr: int = side * 4
    area: int = side ** 2
    diagonal: int = side * math.sqrt(2)
    return perimetr, area, diagonal


if __name__ == "__main__":
    try:
        side_value: int = int(input("Enter the square side value:  "))
    except Exception as e:
        print(f"You enter incorrect information {e} , need int instead")
    perimetr, area, diagonal = square(side_value)
    print(f"Perimetr is {perimetr}\narea is {area}\ndiagonal is {int(diagonal)}")
