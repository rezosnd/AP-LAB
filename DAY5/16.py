numbers = {45, 23, 89, 12, 67, 34, 56, 78, 5, 98}

print("Set of numbers:", numbers)
print()

largest = max(numbers)
smallest = min(numbers)

print(f"Largest element: {largest}")
print(f"Smallest element: {smallest}")
print()

numbers2 = {100, 50, 75, 25, 80, 15}

print("Set of numbers:", numbers2)
print()

print(f"Largest: {max(numbers2)}")
print(f"Smallest: {min(numbers2)}")
print()

sorted_numbers = sorted(numbers)
print("Sorted numbers:", sorted_numbers)
print(f"Largest (from sorted): {sorted_numbers[-1]}")
print(f"Smallest (from sorted): {sorted_numbers[0]}")
