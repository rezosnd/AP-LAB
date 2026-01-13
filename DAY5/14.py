dict1 = {'a': 5, 'b': 15, 'c': 3, 'd': 20, 'e': 8, 'f': 25}

print("Original Dictionary:", dict1)
print()

keys_to_remove = []
for key, value in dict1.items():
    if value < 10:
        keys_to_remove.append(key)

for key in keys_to_remove:
    del dict1[key]

print("After removing values < 10:")
print(dict1)
print()

dict2 = {'x': 2, 'y': 12, 'z': 7, 'w': 18}

print("Original Dictionary:", dict2)
print()

new_dict = {key: value for key, value in dict2.items() if value >= 10}

print("After removing values < 10:")
print(new_dict)
