from library_classes import Book, Library
import storage as st

library = Library()

for book in st.load_books():
    library.books.append(book)

choices = ['\n1. Add book',
    '2. View books',
    '3. Find book',
    '4. Borrow book',
    '5. Return book',
    '6. Exit']

while True:

    print("="*40+"\n\tLIBRARY MANAGEMENT SYSTEM\n"+"="*40)

    for choice in choices:
        print(choice)

    user_choice = input("\nPlease choose from [1-6]: ")


    if user_choice == '1':
        title = input("\nEnter book title: ")

        if library.get_book(title):
            print("\nBook already exists.")
            continue

        author = input("Enter its author: ")

        book = Book(title, author)
        
        library.add_book(book)
        st.save_books(library)


    elif user_choice == '2':
        library.view_books()


    elif user_choice == '3':
        title = input("\nEnter book title: ")
        book = library.get_book(title)

        if book:
            print(book)

        else:
            print("\nBook is not available.")


    elif user_choice == '4':
        title = input("\nBook to be borrowed (Enter title): ")
        library.borrow_book(title)
        st.save_books(library)


    elif user_choice == '5':
        title = input("\nBook to be returned (Enter title): ")
        library.return_book(title)
        st.save_books(library)


    elif user_choice == '6':
        print("\n\tLibrary exited.")
        break

    else:
        print("\nInvalid choice.")
        continue