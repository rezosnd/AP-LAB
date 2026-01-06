string = input("Enter a string: ")

freq_dict = {}

for char in string:
    if char in freq_dict:
        freq_dict[char] += 1
    else:
        freq_dict[char] = 1


print("Character frequencies:", freq_dict)
