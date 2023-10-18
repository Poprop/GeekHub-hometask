# Write a script which accepts decimal number from user and converts it to hexadecimal.
while True:
    decimal_input = int(input())
    hexed_number = hex(decimal_input)
    print(hexed_number)
