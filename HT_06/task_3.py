"""Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000,
и яка вертатиме True, якщо це число просте і False - якщо ні."""


def is_prime(number: int) -> bool:
    if number <= 0:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    try:
        number: int = int(input("Enter your number: "))
    except Exception as e:
        print(f"You get {e} Error , enter valid information")
    print(is_prime(number))
