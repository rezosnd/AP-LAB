numbers = [45, 12, 78, 23, 90, 56, 34]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("List:", numbers)
print("Largest element:", largest)
