my_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 30}

max_key = list(my_dict.keys())[0]
max_value = my_dict[max_key]

for key, value in my_dict.items():
    if value > max_value:
        max_value = value
        max_key = key

print("Key with maximum value:", max_key)
print("Maximum value:", max_value)
