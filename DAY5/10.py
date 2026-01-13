# Dictionary of Book Titles and Authors

# Create dictionary - keys are titles, values are authors
books = {
    'Harry Potter': 'J.K. Rowling',
    'The Hobbit': 'J.R.R. Tolkien',
    '1984': 'George Orwell',
    'Pride and Prejudice': 'Jane Austen',
    'The Great Gatsby': 'F. Scott Fitzgerald'
}

# Print header
print("=== Book Dictionary ===\n")

# Loop through dictionary and print each book with author
for title, author in books.items():
    print(f"{title} by {author}")

# Print specific book's author
print("\n=== Specific Book ===")
print(f"Author of 'Harry Potter': {books['Harry Potter']}")

# Print all titles (keys)
print("\n=== All Titles ===")
print(books.keys())

# Print all authors (values)
print("\n=== All Authors ===")
print(books.values())
