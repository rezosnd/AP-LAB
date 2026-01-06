
numbers = input("Enter numbers separated by space: ").split()
my_list = [int(x) for x in numbers]

unique_list = []

for num in my_list:
    if num not in unique_list:
        unique_list.append(num)

print("List after removing duplicates:", unique_list)
