first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

# Swap values using tuple unpacking for clarity.
first_number, second_number = second_number, first_number

print("After swapping:")
print("First number:", first_number)
print("Second number:", second_number)
