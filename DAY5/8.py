departments = {
    'CS': {'John': 85, 'Alice': 90},
    'ECE': {'Charlie': 88, 'Diana': 92}
}

print("All Departments:", departments)
print()
print("CS Students:", departments['CS'])
print()
print("John's marks:", departments['CS']['John'])
print()

for dept, students in departments.items():
    print(f"{dept}: {students}")
