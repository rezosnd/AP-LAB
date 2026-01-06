list1 = list(map(int, input("Enter elements of first list: ").split()))
list2 = list(map(int, input("Enter elements of second list: ").split()))
for item in list2:
	list1.append(item)
print("Merged list:", list1)


'''It asks the user to enter numbers for the first list and stores them as list1.
It asks the user to enter numbers for the second list and stores them as list2.
For each item in list2, it adds (appends) that item to list1.
Finally, it prints the merged list (list1 with all elements from both lists).'''