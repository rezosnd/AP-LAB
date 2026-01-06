n = int(input("Enter the number of terms: "))

a, b = 0, 1

print(a, end=" ")
if n > 1:
    print(b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c
print()
