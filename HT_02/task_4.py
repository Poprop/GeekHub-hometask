# Write a script which accepts a <number> from
# user and then <number> times asks user for string input.
# At the end script must print out result of concatenating all <number> strings.
num_of_inp = int((input("Please print how many times will you send your input strings ")))
result_string = ""
try_count = num_of_inp
for _ in range(num_of_inp):
    result_string += input(f"Enter some new sting , you have {try_count} try ")
    try_count -= 1
print(result_string)
