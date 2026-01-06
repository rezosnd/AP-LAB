text = input("Enter a string: ")

reversed_text = ""
for char in text:
    reversed_text = char + reversed_text  # prepend each character

print("Reversed string:", reversed_text)