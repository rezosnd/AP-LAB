def count_occurrences(lst, elem):
	count = 0
	for x in lst:
		if x == elem:
			count+=1
	return count

my_list = list(map(int, input("Enter list elements separated by space: ").split()))
element = int(input("Enter element to count: "))
count = count_occurrences(my_list, element)
print(f"{element} occurs {count} times in the list.")

