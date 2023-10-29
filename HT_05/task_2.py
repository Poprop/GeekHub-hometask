"""Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат
(напр. інпут від юзера, результат математичної операції тощо). Також створiть четверту ф-цiю, яка всередині викликає
3 попереднi,
обробляє їх результат та також повертає результат своєї роботи. Таким чином ми будемо викликати одну
(четверту) функцiю, а вона в своєму тiлi - ще 3."""


def plus():
    print("calling 1st func")
    a, b = int(input("enter 1st number for addition ")), int(input("enter second num addition "))
    return a + b


def mult():
    print("calling 2nd func")
    c, d = int(input("enter 1st number for multiply ")), int(input("enter second num for multiply "))
    return c * d


def quadro():
    print("calling 3rd func")
    e = int(input("enter number for squaring "))
    return pow(e, 2)


def multi_task():
    plus_task = plus()
    mult_task = mult()
    quadro_task = quadro()
    return f"The result of my 3 function are :\naddition - {plus_task} ,\n" \
           f"multiply {mult_task} , \n" \
           f"squaring {quadro_task}"


print(multi_task())
