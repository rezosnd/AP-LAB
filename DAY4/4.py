my_list = list(map(int, input("Enter list elements separated by space: ").split()))
unique_list = []
for item in my_list:
	if item not in unique_list:
		unique_list.append(item)
print("List without duplicates:", unique_list)

