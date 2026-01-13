samples = [3, 1, 4, 1, 5, 9, 2]

if not samples:
    print("List is empty")
else:
    mn = mx = samples[0]
    for x in samples[1:]:
        if x < mn:
            mn = x
        if x > mx:
            mx = x
    print(f"List: {samples}")
    print(f"Min: {mn}, Max: {mx}")
    