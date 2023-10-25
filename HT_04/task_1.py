# Написати скрипт, який приймає від користувача два числа (int або float) і робить наступне:
# Кожне введене значення спочатку пробує перевести в int. У разі помилки - пробує перевести в float,
# а якщо і там ловить помилку - пропонує ввести значення ще раз
# (зручніше на даному етапі навчання для цього використати цикл while)
# Виводить результат ділення першого на друге. Якщо при цьому виникає помилка - оброблює її і виводить відповідне
# повідомлення

x = ""
y = ""
while True:
    try:
        x = input("Enter your first float or int number ")
        x = int(x)
        break
    except ValueError:
        print("Invalid number")
        try:
            x = float(x)
            break
        except ValueError:
            print("Invalid number , try again")
while True:
    try:
        y = input("Enter your second float or int number ")
        y = int(y)
        break
    except ValueError:
        print("Invalid number")
        try:
            y = float(y)
        except ValueError:
            print("Invalid number , try again")

try:
    result = x / y
    print(f"Division result: {result}")
except ZeroDivisionError:
    print("Division by zero is not in math logic")
except Exception as e:
    print(f"Error: {e}")
