"""Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів. Після запуска програми на екран
виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
Кожну 1 секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама
як і в звичайних світлофорах (пішоходам зелений тільки коли автомобілям червоний).
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Red
      Yellow     Red
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green"""

import time


def traffic_lights(main_color, transition):
    cars = ["Red"] * main_color + ["Yellow"] * transition + ["Green"] * main_color + ["Yellow"] * transition
    people = ["Green"] * main_color + ["Red"] * transition + ["Red"] * main_color + ["Green"] * transition

    for car, pedestrian in zip(cars, people):
        print(f"{car:15}     {pedestrian}")
        time.sleep(2)


if __name__ == "__main__":
    main_color = 4
    transition_color = 2
    traffic_lights(main_color, transition_color)
# кількість ітерацій дорівнює змінам світлофору в прикладі , можна в принципі поміняти за потреби
