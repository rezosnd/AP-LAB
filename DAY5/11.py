
books = {
    'Harry Potter': 'J.K. Rowling',
    'Chamber of Secrets': 'J.K. Rowling',
    'The Hobbit': 'J.R.R. Tolkien',
    '1984': 'George Orwell',
    'Animal Farm': 'George Orwell',
    'Pride and Prejudice': 'Jane Austen'
}

search_author = input("Enter author name: ")

print(f"\nBooks by {search_author}:\n")

found = False
for book, author in books.items():
    if author == search_author:
        print(f"- {book}")
        found = True

if not found:
    print("No books found by this author!")
