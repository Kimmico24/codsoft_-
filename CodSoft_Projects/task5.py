class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"{contact.name} - {contact.phone}")

    def search_contacts(self, keyword):
        found_contacts = [contact for contact in self.contacts if keyword in contact.name or keyword in contact.phone]
        for contact in found_contacts:
            print(f"{contact.name} - {contact.phone} - {contact.email} - {contact.address}")

    def update_contact(self, name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                self.contacts[i] = new_contact
                return
        print("Contact not found.")

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]


def main():
    manager = ContactManager()

    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(Contact(name, phone, email, address))

        elif choice == "2":
            manager.view_contacts()

        elif choice == "3":
            keyword = input("Enter search keyword: ")
            manager.search_contacts(keyword)

        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            manager.update_contact(name, Contact(new_name, new_phone, new_email, new_address))

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
