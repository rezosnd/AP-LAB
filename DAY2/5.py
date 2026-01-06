text = input("Enter a string: ")

result = ""
seen = set()
for char in text:
	if char not in seen:
		seen.add(char)
		result += char

print("Without duplicates:", result)
