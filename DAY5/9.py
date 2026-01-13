phone_directory = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    phone_directory[name] = phone
    print(f"✓ {name} added!")
    print()

def search_contact():
    name = input("Enter name to search: ")
    if name in phone_directory:
        print(f"{name}: {phone_directory[name]}")
    else:
        print("Contact not found!")
    print()

def update_contact():
    name = input("Enter name to update: ")
    if name in phone_directory:
        new_phone = input("Enter new phone number: ")
        phone_directory[name] = new_phone
        print(f"✓ {name} updated!")
    else:
        print("Contact not found!")
    print()

def delete_contact():
    name = input("Enter name to delete: ")
    if name in phone_directory:
        del phone_directory[name]
        print(f"✓ {name} deleted!")
    else:
        print("Contact not found!")
    print()

def view_all():
    if phone_directory:
        print("=== Phone Directory ===")
        for name, phone in phone_directory.items():
            print(f"{name}: {phone}")
    else:
        print("Directory is empty!")
    print()

while True:
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All")
    print("6. Exit")
    
    choice = input("Choose option (1-6): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        view_all()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
        print()
