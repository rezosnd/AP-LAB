numbers = input("Enter numbers separated by space: ").split()
my_list = [int(x) for x in numbers]
my_list.sort()
print("Sorted list:", my_list)
print("Second largest element is:", my_list[-2])