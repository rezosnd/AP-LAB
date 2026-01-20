def list_stats(lst):
	if not lst:
		raise ValueError("list is empty")
	s = sum(lst)
	avg = s / len(lst)
	return s, avg, max(lst), min(lst)


if __name__ == "__main__":
	try:
		data = input().strip().split()
		nums = [float(x) for x in data]
		if not nums:
			raise ValueError
	except Exception:
		print("Enter space-separated numbers")
	else:
		print(list_stats(nums))

