# Написати функцію <fibonacci>, яка приймає один аргумент
# і виводить всі числа Фібоначчі, що не перевищують його.


def fibonacci(n) -> list:
    fibonacci_nums = [1]
    x1, x2 = 1, 1
    while x2 <= n:
        x1, x2 = x2, x1 + x2
        fibonacci_nums.append(x1)
    return fibonacci_nums


if __name__ == "__main__":
    try:
        number:int=int(input("Enter your maximum fibonacci number: "))
        print(fibonacci(number))
    except Exception as e:
        print(f"You make mistake {e}")
