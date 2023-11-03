# Написати функцію <fibonacci>, яка приймає один аргумент
# і виводить всі числа Фібоначчі, що не перевищують його.


def fibonacci(n):
    fibonacci_nums = [1]
    x1, x2 = 1, 1
    for i in range(n - 1):
        x1, x2 = x2, x1 + x2
        fibonacci_nums.append(x1)
    return fibonacci_nums


print(fibonacci(int(input("Enter your maximum fibonacci number: "))))
