# Write a script which accepts two sequences of comma-separated colors from user.
# Then print out a set containing all the colors from color_list_1 which are not present in color_list_2
color_list1, color_list2 = (set(input("print please coma separated colors").split(",")) for _ in range(2))
unique_colors = color_list1.difference(color_list2)
print(unique_colors)
