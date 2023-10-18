# Write a script which accepts a <number> from user and print
# out a sum of the first <number> positive integers.

# Не зовсім точно поставлено задачу - чи має воно отримувати одразу всі числа
# чи потоковим введенням , тому реалізував 2 варіанти
# __________________1 варіант через список і for з оптовою подачею чисел через кому ________________
# x = list(map(int, input().split(",")))
# res = 0
# for el in x:
#     if el != 0 and el > 0:
#         res += el
#     else:
#         print(res)

# __________________2 варіант через while з потоковим введенням до моменту отримання 0 чи від'ємного числа______________
result = 0
while True:
    number = int(input())
    if number != 0 and number > 0:
        result += number
    else:
        print(result)
        break
