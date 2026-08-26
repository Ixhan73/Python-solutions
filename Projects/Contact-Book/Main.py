from ContactBook import ContactBook, Contact
import json

#=========== STORING AND LOADING CONTACTS USING JSON ============

def store_contacts(book):
    contacts = []

    for contact in book.contacts:
        contacts.append({
            'name': contact.name,
            'phone': contact.phone,
            'email': contact.email
        })

    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            data = json.load(file)

            contacts = []
            for contact in data:
                contacts.append(
                    Contact(
                        contact['name'],
                        contact['phone'],
                        contact['email']
                    )
                )

            return contacts
        
    except (FileNotFoundError, json.JSONDecodeError):
        return []

#==================================================================
#------------------------------------------------------------------
book = ContactBook()
for contact in load_contacts():
    book.contacts.append(contact)

choices = ['\n1.Add contact', '2.View contacts', '3.Find contact', '4.Delete contact', '5.Update contact', '6.Exit']
#------------------------------------------------------------------

#=========== MAIN LOOP FOR THE PROGRAM ============
while True:
    for choice in choices:
        print(choice)

    user_choice = input("\nPlease choose from the above options [1-6]: ")

    # ADDING CONTACT AND STORING IT AS .json
    if user_choice == '1':
        name = input("Enter contact name: ")

        number = input("Number: ")
        if not number.isdigit():
            print("Please enter numbers only!")
            continue
        
        if len(number) != 11:
            print("Number must contain 11 digits.")
            continue

        email = input("Email: ")

        contact_info = Contact(name, number, email)
        book.add_contact(contact_info)
        store_contacts(book)

    # VIEWING CONTACTS FROM .json
    elif user_choice == '2':
        book.view_contacts()

    # FINDING A CONTACT
    elif user_choice == '3':
        contact_to_find = input("Enter contact name: ")
        book.find_contact(contact_to_find)

    # DELETING A CONTACT
    elif user_choice == '4':
        contact_to_delete = input("Enter contact name: ")
        book.del_contact(contact_to_delete)
        store_contacts(book)

    # UPDATING AN EXISTING CONTACT
    elif user_choice == '5':
        name = input("Enter contact name: ")
        book.update_contact(name)
        store_contacts(book)

    # EXITING THE PROGRAM
    elif user_choice == '6':
        print("Contact book closed!")
        break

    else:
        print("\nPlease enter from given choices!\n")
        continue