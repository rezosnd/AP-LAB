
import os

def count_characters_in_file(filename):

	if not os.path.isfile(filename):

		script_dir = os.path.dirname(os.path.abspath(__file__))
		filename = os.path.join(script_dir, filename)
	try:
		with open(filename, 'r', encoding='utf-8') as file:
			content = file.read()
			print(f"Total characters: {len(content)}")
	except FileNotFoundError:
		print(f"File '{filename}' not found.")
	except Exception as e:
		print(f"An error occurred: {e}")

if __name__ == "__main__":
	filename = input("Enter the filename: ")
	count_characters_in_file(filename)
