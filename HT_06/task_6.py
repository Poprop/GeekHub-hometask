"""Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку.
Тобто функція приймає два аргументи: список і величину зсуву (якщо ця величина додатня - пересуваємо з кінця на початок,
якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
   fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
   fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]"""


def shift_func(nums, shift):
    if len(nums) >= shift:
        return nums[-shift:] + nums[:-shift]
    if len(nums) <= shift:
        print("Dude, I asked you to enter less number for the bottom of the list, now I need to write even more code.\n"
              "That is your result , but next time try to play on the rules")
        shift = shift % len(nums)
        return nums[-shift:] + nums[:-shift]


nums_list = [int(i) for i in
             input("Enter numbers in one string using 'Space' button and finish by 'Enter' button: ").split()]
shift_value = (int(input("Enter shift value , but try to chose value less then amount of entered numbers in list: ")))
print(shift_func(nums_list, shift_value))
