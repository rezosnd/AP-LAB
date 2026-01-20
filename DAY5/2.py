sentence = "hello world hello python world hello"

words = sentence.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1
                   
print("Sentence:", sentence)
print("\nWord Frequency:")
for word, count in freq.items():
    print(f"{word} : {count}")
