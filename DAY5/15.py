dict1 = {'a': 45, 'b': 23, 'c': 89, 'd': 12, 'e': 67}

print("Dictionary:", dict1)
print()

max_value = max(dict1.values())
min_value = min(dict1.values())

print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
print()

max_key = max(dict1, key=dict1.get)
min_key = min(dict1, key=dict1.get)

print(f"Key with maximum value: {max_key} = {dict1[max_key]}")
print(f"Key with minimum value: {min_key} = {dict1[min_key]}")
print()

dict2 = {'john': 85, 'alice': 92, 'bob': 78, 'charlie': 95}

print("Dictionary:", dict2)
print()

print(f"Maximum value: {max(dict2.values())}")
print(f"Minimum value: {min(dict2.values())}")
