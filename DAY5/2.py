# Count Frequency of Words in a Sentence - Simple Version

sentence = "hello world hello python world hello"

# Split sentence into words
words = sentence.split()

# Create dictionary
freq = {}

# Count frequency
for word in words:
    freq[word] = freq.get(word, 0) + 1

# Print results
print("Sentence:", sentence)
print("\nWord Frequency:")
for word, count in freq.items():
    print(f"{word} : {count}")
