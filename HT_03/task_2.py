# Write a script to remove an empty elements from a list.

test_list = [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]
result_list = [el for el in test_list if el]
