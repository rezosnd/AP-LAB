# Script to copy content from one file to another
def copy_file_content(src, dest):
	try:
		with open(src, 'r', encoding='utf-8') as fsrc:
			content = fsrc.read()
		with open(dest, 'w', encoding='utf-8') as fdest:
			fdest.write(content)
		print(f"Content copied from {src} to {dest}.")
	except FileNotFoundError:
		print(f"Source file '{src}' not found.")
	except Exception as e:
		print(f"An error occurred: {e}")

if __name__ == "__main__":
	src = input("Enter the source filename: ")
	dest = input("Enter the destination filename: ")
	copy_file_content(src, dest)
