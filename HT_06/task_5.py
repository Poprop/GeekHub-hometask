# Написати функцію <fibonacci>, яка приймає один аргумент
# і виводить всі числа Фібоначчі, що не перевищують його.


def fibonacci(n)->int:
    fibonacci_nums = [1]
    x1, x2 = 1, 1
    while x2 <= n:
        x1, x2 = x2, x1 + x2
        fibonacci_nums.append(x1)
    return fibonacci_nums

if __name__ == "__main__":
    print(fibonacci(int(input("Enter your maximum fibonacci number: "))))
