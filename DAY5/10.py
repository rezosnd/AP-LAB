books = {
    'Harry Potter': 'J.K. Rowling',
    'The Hobbit': 'J.R.R. Tolkien',
    '1984': 'George Orwell',
    'Pride and Prejudice': 'Jane Austen',
    'The Great Gatsby': 'F. Scott Fitzgerald'
}

print("=== Book Dictionary ===\n")

for title, author in books.items():
    print(f"{title} by {author}")

print("\n=== Specific Book ===")
print(f"Author of 'Harry Potter': {books['Harry Potter']}")

print("\n=== All Titles ===")
print(books.keys())

print("\n=== All Authors ===")
print(books.values())
