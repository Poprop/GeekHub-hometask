"""Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку.
Тобто функція приймає два аргументи: список і величину зсуву (якщо ця величина додатня - пересуваємо з кінця на початок,
якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
   fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
   fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]"""


def shift_func(nums, shift) -> list:
    shift: int = shift % len(nums)
    return nums[-shift:] + nums[:-shift]



if __name__ == "__main__":
    try:
        nums_list:list = [int(i) for i in
                     input("Enter numbers in one string using 'Space' button and finish by 'Enter' button: ").split()]
        shift_value:int = (int(input("Enter shift value: ")))
        print(shift_func(nums_list, shift_value))
    except Exception as e:
        print(f"Something in your input is wrong {e}")
