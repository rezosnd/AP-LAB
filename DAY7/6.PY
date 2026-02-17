marks = {
    "Math": 85,
    "English": 90,
    "Science": 78,
    "History": 88,
    "Computer": 92
}

print("Dictionary:", marks)
print()

total = 0

for subject in marks:
    value = marks[subject]
    total = total + value

print("Sum of all values:", total)
print("Average:", total / len(marks))
