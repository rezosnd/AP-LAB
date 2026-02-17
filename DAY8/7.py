import csv

# Script to store student records in a CSV file
def add_student_record(filename, student_data):
	try:
		file_exists = False
		try:
			with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
				file_exists = True
		except FileNotFoundError:
			pass
		with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
			fieldnames = ['Roll No', 'Name', 'Marks']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			if not file_exists:
				writer.writeheader()
			writer.writerow(student_data)
		print(f"Student record added to {filename}.")
	except Exception as e:
		print(f"An error occurred: {e}")

if __name__ == "__main__":
	filename = input("Enter the CSV filename: ")
	roll_no = input("Enter Roll No: ")
	name = input("Enter Name: ")
	marks = input("Enter Marks: ")
	student_data = {'Roll No': roll_no, 'Name': name, 'Marks': marks}
	add_student_record(filename, student_data)
