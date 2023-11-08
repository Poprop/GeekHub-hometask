"""Напишіть функцію,яка приймає на вхід рядок та повертає кількість окремих регістро-незалежних букв
та цифр, які зустрічаються в рядку більше ніж 1 раз. Рядок буде складатися лише з цифр та букв (великих і малих).
Реалізуйте обчислення за допомогою генератора.
    Example (input string -> result):
    "abcde" -> 0            # немає символів, що повторюються
    "aabbcde" -> 2          # 'a' та 'b'
    "aabBcde" -> 2          # 'a' присутнє двічі і 'b' двічі (`b` та `B`)
    "indivisibility" -> 1   # 'i' присутнє 6 разів
    "Indivisibilities" -> 2 # 'i' присутнє 7 разів та 's' двічі
    "aA11" -> 2             # 'a' і '1'
    "ABBA" -> 2             # 'A' і 'B' кожна двічі"""


def count_generator(iterable_string: str) -> int:
    counter = {}
    for el in iterable_string:
        counter[el.lower()] = counter.get(el.lower(), 0) + 1
    for el, count in counter.items():
        if count > 1:
            yield el


def result(generator) -> int:
    return len(list(generator))


if __name__ == "__main__":
    print(result("aabBcde"))
    print(result('aabbcde'))
    print(result('aabBcde'))
    print(result('indivisibility'))
    print(result('Indivisibilities'))
    print(result('aA11'))
