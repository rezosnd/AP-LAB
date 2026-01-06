list1 = list(map(int, input("Enter elements of first list: ").split()))
list2 = list(map(int, input("Enter elements of second list: ").split()))
for item in list2:
	list1.append(item)
print("Merged list:", list1)
