# Script to append data to a file
def append_to_file(filename, data):
	try:
		with open(filename, 'a', encoding='utf-8') as file:
			file.write(data)
		print(f"Data appended to {filename}.")
	except Exception as e:
		print(f"An error occurred: {e}")

if __name__ == "__main__":
	filename = input("Enter the filename to append to: ")
	data = input("Enter the data to append: ")
	append_to_file(filename, data)
