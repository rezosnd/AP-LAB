# Create Dictionary with Words as Keys and Their Lengths as Values

words = ['hello', 'world', 'python', 'code', 'dictionary']

print("Words:", words)
print()

word_length = {}
for word in words:
    word_length[word] = len(word)

print("Dictionary (Word: Length):")
print(word_length)
print()

print("Formatted Output:")
for word, length in word_length.items():
    print(f"{word} - {length} characters")
