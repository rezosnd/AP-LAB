# Simple code to rotate a list right by given positions
lst = [1, 2, 3, 4, 5]
positions = 2
positions = positions % len(lst)
rotated = lst[-positions:] + lst[:-positions]
print(rotated)
