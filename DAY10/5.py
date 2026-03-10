import numpy as np

my_list = [10, 20, 30, 40, 50]

arr = np.array(my_list)

print("List:", my_list)
print("NumPy Array:", arr)
print("Type:", type(arr))

print("\nArithmetic Operations:")
print("Addition (arr + 5)      :", arr + 5)
print("Subtraction (arr - 5)   :", arr - 5)
print("Multiplication (arr * 2):", arr * 2)
print("Division (arr / 2)      :", arr / 2)
print("Power (arr ** 2)        :", arr ** 2)

print("\nStatistical Operations:")
print("Sum    :", np.sum(arr))
print("Mean   :", np.mean(arr))
print("Median :", np.median(arr))
print("Std Dev:", np.std(arr))
print("Min    :", np.min(arr))
print("Max    :", np.max(arr))

print("\nArray Properties:")
print("Shape :", arr.shape)
print("Size  :", arr.size)
print("Dtype :", arr.dtype)
