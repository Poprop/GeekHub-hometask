# 1. Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції
# з 2-ма числами, а саме додавання, віднімання, множення, ділення.
# - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення.
# - Якщо використати один з методів - last_result повенен повернути результат виконання ПОПЕРЕДНЬОГО методу.
#     Example:
#     last_result --> None
#     1 + 1
#     last_result --> None
#     2 * 3
#     last_result --> 2
#     3 * 4
#     last_result --> 6

class Calc:
    def __init__(self):
        self.result_list = [None, None]

    def addition(self, x, y):
        result = x + y
        self.result_list.append(result)
        self.result_list = self.result_list[1:]
        return f"{x} + {y}"

    def subtraction(self, x, y):
        result = x - y
        self.result_list.append(result)
        self.result_list = self.result_list[1:]
        return f"{x} - {y}"

    def division(self, x, y):
        try:
            result = x / y
            self.result_list.append(result)
            self.result_list = self.result_list[1:]
            return f"{x} / {y}"
        except ZeroDivisionError:
            print("Cant divide by 0 ")

    def multiplication(self, x, y):
        result = x * y
        self.result_list.append(result)
        self.result_list = self.result_list[1:]
        return f"{x} * {y}"

    @property
    def last_result(self):
        return self.result_list[0]


calc = Calc()
print(calc.last_result)
print(calc.addition(1, 1))
print(calc.last_result)
print(calc.multiplication(2, 3))
print(calc.last_result)
print(calc.multiplication(3, 4))
print(calc.last_result)
