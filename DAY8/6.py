import logging

# Configure logging to write error messages to a log file
logging.basicConfig(filename='error.log',
					filemode='a',
					format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.ERROR)

def do_something():
	try:
		# Example code that may raise an error
		x = 1 / 0
	except Exception as e:
		logging.error(f"An error occurred: {e}")
		print("Error logged to error.log")

if __name__ == "__main__":
	do_something()
