"""Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12) та яка буде повертати пору року,
 якiй цей мiсяць належить (зима, весна, лiто або осiнь). У випадку некоректного введеного значення - виводити
 відповідне повідомлення."""


def season(month_num):
    four_seasons = {(12, 1, 2): "winter",
                    (3, 4, 5): "spring",
                    (6, 7, 8): "summer",
                    (9, 10, 11): "autumn"}
    try:
        month_number = int(month_num)
        if month_number not in range(1, 13):
            return "your month number is invalid"
        else:
            for months, season in four_seasons.items():
                if month_number in months:
                    return season

    except ValueError:
        return "You input something else but not the month number"


print(season(input("Input your month number: ")))
