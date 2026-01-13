set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

print("Set 1:", set1)
print("Set 2:", set2)
print()

if set1.issubset(set2):
    print("✓ Set 1 is a subset of Set 2")
else:
    print("✗ Set 1 is NOT a subset of Set 2")

print()

if set1 <= set2:
    print("✓ Set 1 is a subset of Set 2 (using <=)")
else:
    print("✗ Set 1 is NOT a subset of Set 2")

print()

set3 = {1, 2, 3}
set4 = {1, 2}

print("Set 3:", set3)
print("Set 4:", set4)
print()

if set4.issubset(set3):
    print("✓ Set 4 is a subset of Set 3")
else:
    print("✗ Set 4 is NOT a subset of Set 3")

print()

set5 = {10, 20}
set6 = {5, 15}

print("Set 5:", set5)
print("Set 6:", set6)
print()

if set5.issubset(set6):
    print("✓ Set 5 is a subset of Set 6")
else:
    print("✗ Set 5 is NOT a subset of Set 6")
