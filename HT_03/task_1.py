# Write a script that will run through a list of tuples and replace the last value for each tuple.
# The list of tuples can be hardcoded. The "replacement" value is entered by user.
# The number of elements in the tuples must be different.

tuple_list = [("shadow company", 1, "shepard"), ("russian shit",5, "makarov", 2, "zakhaiev", 6, "hex"),
              ("special force",3, "rouch", "ghost", "price","nikolay")]

for i in range(len(tuple_list)):
    tuple_list[i] = tuple_list[i][:-1] + (input("enter your replace value "), )

print(tuple_list)
