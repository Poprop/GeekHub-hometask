# Write a script to concatenate all elements in a list into a string
# and print it. List must be include both strings and integers and must be hardcoded.

hardcoded_list = [3, "pen", 5, "pineapple", 4, "apple", 7, "pen"]
print("".join(list(map(str, hardcoded_list))))
