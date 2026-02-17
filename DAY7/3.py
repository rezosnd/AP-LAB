numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("List:", numbers)
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)
