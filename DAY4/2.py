

# Function to count how many times 'elem' appears in 'lst' (without using 'in')
def count_occurrences(lst, elem):
	count = 0
	for x in lst:
		if x == elem:
			count += 1
	return count

# Read list and element from user, then count occurrences
my_list = list(map(int, input("Enter list elements separated by space: ").split()))
element = int(input("Enter element to count: "))
count = count_occurrences(my_list, element)
print(f"{element} occurs {count} times in the list.")



'''It asks the user to enter numbers separated by spaces and stores them as a list of integers called my_list.
It then asks the user to enter a number (element) to count in the list.
The code counts how many times that number appears in the list using the count() method.
Finally, it prints how many times the number occurs in the list.'''