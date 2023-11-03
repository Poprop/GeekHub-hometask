"""Написати функцію, яка приймає на вхід список (через кому), підраховує кількість однакових елементів у ньомy
і виводить результат. Елементами списку можуть бути дані будь-яких типів."""


def counter_func(entered_list):
    counter = {}
    for el in entered_list:
        if isinstance(el, list):
            el = tuple(el)
        if el not in counter:
            counter[el] = 1
        else:
            counter[el] += 1
    return counter


print(counter_func([1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]]))
