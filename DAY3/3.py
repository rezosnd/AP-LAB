# my_list = [10, 20, 4, 45, 99]
numbers = input("Enter numbers separated by space: ").split()
my_list = [int(x) for x in numbers]
max_element = my_list[0]

for num in my_list:
    if num > max_element:
        max_element = num

# Print the result
print("The largest element in the list is:", max_element)
