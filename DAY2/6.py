import re

pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$")

email = input("Enter an email: ")

if pattern.match(email):
	print("Valid email format")
else:
	print("Invalid email format")
