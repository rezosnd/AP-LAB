import string

# Script to read a file and remove punctuation
def remove_punctuation_from_file(filename):
	try:
		with open(filename, 'r', encoding='utf-8') as file:
			content = file.read()
		no_punct = content.translate(str.maketrans('', '', string.punctuation))
		print("Content without punctuation:")
		print(no_punct)
	except FileNotFoundError:
		print(f"File '{filename}' not found.")
	except Exception as e:
		print(f"An error occurred: {e}")

if __name__ == "__main__":
	filename = input("Enter the filename: ")
	remove_punctuation_from_file(filename)
