
# Function to remove duplicates from a list without using 'in'
def remove_duplicates(lst):
	unique = []
	for i in range(len(lst)):
		found = False
		for j in range(len(unique)):
			if lst[i] == unique[j]:
				found = True
				break
		if not found:
			unique.append(lst[i])
	return unique

my_list = list(map(int, input("Enter list elements separated by space: ").split()))
unique_list = remove_duplicates(my_list)
print("List without duplicates:", unique_list)