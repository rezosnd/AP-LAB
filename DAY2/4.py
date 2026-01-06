rows = int(input("Enter number of rows: "))

print("Normal triangle:")
for i in range(1, rows + 1):
	print("*" * i)

print("Inverted triangle:")
for i in range(rows, 0, -1):
	print("*" * i)