number = int(input("Enter a number: "))
digits = len(str(number))

temp = number
total = 0
while temp > 0:
	digit = temp % 10
	total += digit ** digits
	temp //= 10

if total == number:
	print("Armstrong number")
else:
	print("Not an Armstrong number")
