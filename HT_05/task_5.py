"""Ну і традиційно - калькулятор :slightly_smiling_face: Повинна бути 1 ф-цiя, яка б приймала 3 аргументи - один з
яких операцiя, яку зробити! Аргументи брати від юзера (можна по одному - 2, окремо +, окремо 2; можна всі разом -
типу 1 + 2). Операції що мають бути присутні: +, -, *, /, %, //, **. Не забудьте протестувати з різними значеннями
на предмет помилок!"""


def calculator():
    try:
        number_1 = int(input("Enter the first operand: "))
        number_2 = int(input("Enter the second operand: "))
        operation = input("Enter the operation (+, -, *, /, %, //, **): ")

        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else "Division by zero is not allowed.",
            '%': lambda x, y: x % y,
            '//': lambda x, y: x // y if y != 0 else "Floor division by zero is not allowed.",
            '**': lambda x, y: x ** y
        }
        result = operations.get(operation, lambda x, y: "You enter invalid operation try next "
                                                        "time use one of this opperation:\n+ addition\n- subtraction\n"
                                                        "* multiply\n/ division\n% modulus\n"
                                                        "// floor division\n** exponentiation")(number_1, number_2)

        return (f"{number_1} {operation} {number_2} = {result}")

    except ValueError:
        return ("Enter an integer value, not str or smth else , it`s a simple calculator , not more .")
    except Exception as e:
        return (f"Dat is very strange and unpredictable error : {e}")


print(calculator())
