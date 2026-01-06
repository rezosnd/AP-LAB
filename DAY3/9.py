def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Enter a positive number")
else:
    result = sum_natural(num)
    print(f"The sum of first {num} natural numbers is {result}")
