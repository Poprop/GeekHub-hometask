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


def my_range(start: int, end: int, step: int = 1) -> int:
    if step > 0 and end > start:
        i = start
        while i < end:
            yield i
            i += step
    elif step < 0 and end < start:
        i = start
        while i > end:
            yield i
            i += step
    else:
        return iter(())


if __name__ == "__main__":
    start = int(input("Enter start of iteration: "))
    stop = int(input("Enter end of iteration: "))
    step = int(input("Enter step of iteration: "))

    a = my_range(start, stop, step)
try:
    for i in range(stop + 1):
        print(next(a))
except StopIteration:
    print("В ітераторі не залишилось елементів")
