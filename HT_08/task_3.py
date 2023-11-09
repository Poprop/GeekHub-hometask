"""Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції. Тобто щоб її можна було використати у вигляді:
    for i in my_range(1, 10, 2):
        print(i)
    1
    3
    5
    7
    9
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
   P.P.P.S Не забудьте обробляти невалідні ситуації (аналог range(1, -10, 5)). Подивіться як веде себе стандартний range в таких випадках."""


def my_range(end, start=0, step=1):
    current = start
    while current < end:
        yield current
        current += step


if __name__ == "__main__":
    end = int(input("Enter end of iteration: "))
    try:
        start = int(input("Enter start of iteration: "))
    except ValueError:
        start = 0

    try:
        step = int(input("Enter step of iteration: "))
    except ValueError:
        step = 1

    a = my_range(end, start, step)
try:
    for i in a:
        print(i)
except StopIteration:
    print("В ітераторі не залишилось елементів")
