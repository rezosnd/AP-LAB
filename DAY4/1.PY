def find_min_max(nums):
	if not nums:
		raise ValueError("find_min_max() arg is an empty list")
	mn = mx = nums[0]
	for x in nums[1:]:
		if x < mn:
			mn = x
		if x > mx:
			mx = x
	return mn, mx


if __name__ == "__main__":
	samples = [3, 1, 4, 1, 5, 9, 2]
	mn, mx = find_min_max(samples)
	print(f"List: {samples}")
	print(f"Min: {mn}, Max: {mx}")

