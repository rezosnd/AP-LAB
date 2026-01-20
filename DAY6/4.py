def list_stats(nums):
    total = sum(nums)
    average = total / len(nums)
    maximum = max(nums)
    minimum = min(nums)

    return total, average, maximum, minimum


nums = [10, 20, 30, 40]

result = list_stats(nums)
print(result)
