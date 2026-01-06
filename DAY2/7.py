import re

text = input("Enter a string: ")

numbers = re.findall(r"\d+", text)

print("Numbers found:", numbers)
