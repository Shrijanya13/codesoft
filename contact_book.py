# Contact management system

contacts = {}

def add_contact():
    """Add a new contact"""
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter home address: ")

    if name in contacts:
        print("This contact already exists!")
    else:
        contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print(f"Contact for {name} added successfully!")

def view_contacts():
    """View all contacts"""
    if contacts:
        print("\n--- Contact List ---")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}")
        print("---------------------\n")
    else:
        print("No contacts found!")

def search_contact():
    """Search for a contact by name or phone number"""
    search_term = input("Enter the contact name or phone number to search: ").lower()
    found = False

    for name, info in contacts.items():
        if search_term == name.lower() or search_term == info['phone']:
            print(f"\nContact found: \nName: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}")
            found = True
            break

    if not found:
        print("Contact not found.")

def update_contact():
    """Update a contact's details"""
    name = input("Enter the name of the contact to update: ")

    if name in contacts:
        print(f"Updating contact for {name}...")
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ")
        email = input(f"Enter new email (current: {contacts[name]['email']}): ")
        address = input(f"Enter new address (current: {contacts[name]['address']}): ")

        contacts[name]['phone'] = phone
        contacts[name]['email'] = email
        contacts[name]['address'] = address

        print(f"Contact for {name} updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    """Delete a contact"""
    name = input("Enter the name of the contact to delete: ")

    if name in contacts:
        del contacts[name]
        print(f"Contact for {name} deleted successfully!")
    else:
        print("Contact not found.")

def display_menu():
    """Display the main menu"""
    print("""
    --- Contact Manager ---
    1. Add Contact
    2. View All Contacts
    3. Search Contact
    4. Update Contact
    5. Delete Contact
    6. Exit
    """)

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
