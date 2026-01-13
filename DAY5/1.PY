student = {
    'Name': 'John Doe',
    'Roll_No': 101,
    'Class': '10A',
    'Marks': 85,
    'Subject': 'Python'
}

print("Keys:")
print(student.keys())

print("\nValues:")
print(student.values())

print("\nKeys and Values:")
for key, value in student.items():
    print(f"{key}: {value}")
