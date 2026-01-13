dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 2, 'c': 3}

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print()

if dict1 == dict2:
    print("✓ Dictionaries are identical!")
else:
    print("✗ Dictionaries are NOT identical!")

print("\n---\n")

dict3 = {'a': 1, 'b': 2, 'c': 3}
dict4 = {'a': 1, 'b': 2, 'c': 5}

print("Dictionary 3:", dict3)
print("Dictionary 4:", dict4)
print()

if dict3 == dict4:
    print("✓ Dictionaries are identical!")
else:
    print("✗ Dictionaries are NOT identical!")

print("\n---\n")

dict5 = {'a': 1, 'b': 2}
dict6 = {'a': 1, 'b': 2, 'c': 3}

print("Dictionary 5:", dict5)
print("Dictionary 6:", dict6)
print()

if dict5 == dict6:
    print("✓ Dictionaries are identical!")
else:
    print("✗ Dictionaries are NOT identical!")
