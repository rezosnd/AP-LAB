
m1 = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
m2 = [
	[9, 8, 7],
	[6, 5, 4],
	[3, 2, 1]
]

add = []
sub = []
for i in range(len(m1)):
	m1 = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	]
	m2 = [
		[9, 8, 7],
		[6, 5, 4],
		[3, 2, 1]
	]

	print("Addition:")
	for i in range(len(m1)):
		print([m1[i][j] + m2[i][j] for j in range(len(m1[0]))])

	print("Subtraction:")
	for i in range(len(m1)):
		print([m1[i][j] - m2[i][j] for j in range(len(m1[0]))])
