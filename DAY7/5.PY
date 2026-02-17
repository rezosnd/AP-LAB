student = {
    "name": "REHAN",
    "age": 20,
    "city": "RANCHI",
    "grade": "A"
}

print("Dictionary:", student)
print()

key1 = "name"
if key1 in student:
    print(key1, "exists in dictionary")
    print("Value:", student[key1])
else:
    print(key1, "does not exist in dictionary")

print()

# Check another key
key2 = "phone"
if key2 in student:
    print(key2, "exists in dictionary")
    print("Value:", student[key2])
else:
    print(key2, "does not exist in dictionary")
