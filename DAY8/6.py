import logging

logging.basicConfig(filename='error.log',
					filemode='a',
					format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.ERROR)

def do_something():
	try:
		x = 1 / 0
	except Exception as e:
		logging.error(f"An error occurred: {e}")
		print("Error logged to error.log")

if __name__ == "__main__":
	do_something()
