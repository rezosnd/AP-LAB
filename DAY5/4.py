set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)
print()

union = set1 | set2
print("Union (|):", union)
print("Union (union()):", set1.union(set2))
print()


intersection = set1 & set2
print("Intersection (&):", intersection)
print("Intersection (intersection()):", set1.intersection(set2))
print()

difference1 = set1 - set2
print("Difference (set1 - set2):", difference1)
print("Difference (difference()):", set1.difference(set2))
print()

difference2 = set2 - set1
print("Difference (set2 - set1):", difference2)
print()

sym_diff = set1 ^ set2
print("Symmetric Difference (^):", sym_diff)
print("Symmetric Difference (symmetric_difference()):", set1.symmetric_difference(set2))
