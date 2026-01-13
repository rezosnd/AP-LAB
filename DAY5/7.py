my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original Dictionary:", my_dict)
print()

tuple_list = list(my_dict.items())
print("Converted to List of Tuples:", tuple_list)
print()

back_to_dict = dict(tuple_list)
print("Converted back to Dictionary:", back_to_dict)
