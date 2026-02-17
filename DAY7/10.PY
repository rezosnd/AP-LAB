keys = ["name", "age", "city"]
values = ["REHAN", 20, "RANCHI"]

student = dict(zip(keys, values))

print("Dictionary:", student)
for key in student:
    print(key, ":", student[key])
