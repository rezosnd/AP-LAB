my_list = list(map(int, input("Enter list elements separated by space: ").split()))
element = int(input("Enter element to count: "))
count = my_list.count(element)
print(f"{element} occurs {count} times in the list.")