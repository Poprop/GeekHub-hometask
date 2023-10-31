"""Наприклад маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfe  kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345" -> просто потицяв по клавi =)
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього та яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр лише з буквами (без пробілів)
-  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)"""

import collections
import re


def task(string):
    if 30 <= len(string) <= 50:
        numbers = len([i for i in string if i.isdigit()])
        letters = len(re.findall(r'[A-Za-zА-Яа-я]', string))
        return (f"Your string which lenght is {len(string)} has: \n{letters} letters\n{numbers} numbers")

    if len(string) < 30:
        summary = (re.findall(r'\d+', string))
        new_string = "".join(re.findall(r'[A-Za-zА-Яа-я]', string))

        return f"Cума всіх чисел {summary} рядка - {sum(map(int, summary))},\nлітери з рядка - {new_string}"
    if len(string) > 50:
        int_list = []
        alph_list = []
        for el in string:
            if el.isdigit():
                int_list.append(el)
            elif el.isalpha():
                alph_list.append(el)
        return f"Кількість повторів числел {dict(collections.Counter(int_list))}, \n" \
               f"кількість повторів літер {dict(collections.Counter(alph_list))}"


print(task("feroi334324укewdew224241  апукс22іeпепек о en3c0"))
