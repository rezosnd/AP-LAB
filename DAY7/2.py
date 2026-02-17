numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]

unique_list = []

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("Original list:", numbers)
print("List without duplicates:", unique_list)
