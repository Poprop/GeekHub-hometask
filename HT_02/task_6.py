# Write a script to check whether a value from user input is contained in a group of values.
# e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
#      [1, 2, 'u', 'a', 4, True] --> 5 --> False

test_list = [1, 2, 'u', 'a', 4, True]
converted_list = list(map(str, test_list))
while True:
    print(input("Please input element for check if it in collection") in converted_list)
