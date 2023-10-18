# Write a script which accepts a sequence of comma-separated numbers
# from user and generate a list and a tuple with those numbers.

x = list(map(int, input().split(",")))
y = tuple(x)
print(f"Це свіжозгенерований список {x}")
print(f"Це свіжозгенерований кортеж {y}")
