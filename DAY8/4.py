# Script to count lines, words, and characters in a file
def count_file_stats(filename):
	try:
		with open(filename, 'r', encoding='utf-8') as file:
			lines = file.readlines()
			num_lines = len(lines)
			num_words = sum(len(line.split()) for line in lines)
			num_chars = sum(len(line) for line in lines)
		print(f"Lines: {num_lines}")
		print(f"Words: {num_words}")
		print(f"Characters: {num_chars}")
	except FileNotFoundError:
		print(f"File '{filename}' not found.")
	except Exception as e:
		print(f"An error occurred: {e}")

if __name__ == "__main__":
	filename = input("Enter the filename: ")
	count_file_stats(filename)
