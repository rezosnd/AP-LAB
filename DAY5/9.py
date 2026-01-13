phone_book = {'John': '9876543210', 'Alice': '9123456789'}

phone_book['Bob'] = '9555666777'
print("Added Bob\n")

name = 'John'
if name in phone_book:
    print(f"Found: {name} - {phone_book[name]}\n")

phone_book['Alice'] = '9111222333'
print("Updated Alice\n")

del phone_book['Bob']
print("Deleted Bob\n")

print("All Contacts:")
for name, phone in phone_book.items():
    print(f"{name}: {phone}")
