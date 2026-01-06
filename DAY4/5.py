
# Simple bubble sort for ascending and descending order (no 'in' used)
def bubble_sort(lst, reverse=False):
	arr = lst[:]
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if (not reverse and arr[j] > arr[j+1]) or (reverse and arr[j] < arr[j+1]):
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr

my_list = list(map(int, input("Enter list elements separated by space: ").split()))
asc = bubble_sort(my_list)
desc = bubble_sort(my_list, reverse=True)
print("Ascending order:", asc)
print("Descending order:", desc)
