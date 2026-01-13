
student = {
    'Name': 'John Doe',
    'Roll_No': 101,
    'Class': '10A',
    'Marks': 85,
    'Subject': 'Python'
}

# Print all keys
print("Keys:")
print(student.keys())

# Print all values
print("\nValues:")
print(student.values())

# Print keys and values together
print("\nKeys and Values:")
for key, value in student.items():
    print(f"{key}: {value}")
