my_list = list(map(int, input("Enter list elements separated by space: ").split()))
reversed_list = my_list[::-1]
print("Reversed list:", reversed_list)


'''It asks the user to enter numbers separated by spaces and stores them as a list of integers called my_list.
It creates a new list called reversed_list, which contains the elements of my_list in reverse order (using slicing with [::-1]).
It prints the reversed list.'''