import pandas as pd

# Script to read a CSV file using pandas and print the first 5 rows
def print_first_five_rows(filename):
	try:
		df = pd.read_csv(filename)
		print("First 5 rows:")
		print(df.head())
	except FileNotFoundError:
		print(f"File '{filename}' not found.")
	except Exception as e:
		print(f"An error occurred: {e}")

if __name__ == "__main__":
	filename = input("Enter the CSV filename: ")
	print_first_five_rows(filename)
