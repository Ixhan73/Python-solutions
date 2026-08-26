#-----------------------------------------------------------------------------
class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name.title()}\n Phone: {self.phone}\n Email: {self.email}\n"

#------------------------------------------------------------------------------
class ContactBook:

    def __init__(self):
        self.contacts = []


    #======= ADDING A NEW CONTACT =======
    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Added {contact.name.title()} successfully!")


    #======= VIEWING CONTACTS =======
    def view_contacts(self):
        if not self.contacts:
            print("No contacts stored.")
            return

        for contact in self.contacts:
            print(contact) 


    #======= FINDING A CONTACT =======
    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return contact
            
        print("Contact not found.")
        return None


    #======= DELETING A CONTACT =======
    def del_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact of {name} removed successfully.")
                return
            
        print("Contact not found")


    #======= UPDATING A CONTACT =======
    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("What do you want to update\n1.Name\n2.Phone\n3.Email")
                choice = input("Enter 1-3: ")
                if choice == '1':
                    new_name = input("Enter new name: ")
                    contact.name = new_name
                    print("Name updated!\n")

                elif choice == '2':
                    new_phone = input("Enter new number: ")
                    if not new_phone.isdigit():
                        print("Please enter numbers only!")
                        return
                            
                    if len(new_phone) != 11:
                        print("Number must contain 11 digits.")
                        return

                    contact.phone = new_phone
                    print("Phone number updated!\n")

                elif choice == '3':
                    new_email = input("Enter new email: ")
                    contact.email = new_email
                    print("Email updated!\n")

                else:
                    print("Invalid choice.")

                return

        print("Contact not found.")