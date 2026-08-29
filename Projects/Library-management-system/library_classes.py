
#================= BOOK OBJECT ================
class Book:

    def __init__(self, title, author, available='Yes'):

        self.title = title 
        self.author = author
        self.available = available

    def __str__(self):
        return f"\nTitle: {self.title.title()}\nAuthor: {self.author.title()}\nAvailable: {self.available}"
    

#============== LIBRARY OBJECT ================
class Library:

    def __init__(self):

        self.books = []


    #=== ADDING A BOOK
    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.title.lower() == book.title.lower():
                print("\nBook already exists.")
                return

        self.books.append(book)
        print(f'''\n\tAdded "{book.title}" to the library.''')
#-------------------------------------------------------------
    #=== VIEWING BOOKS
    def view_books(self):
        if not self.books:
            print("\nNo books in library.")
            return

        for book in self.books:
            print('\n',book)
#-------------------------------------------------------------
    #=== FINDING A BOOK
    def get_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book

        return None
#-------------------------------------------------------------
    #=== BORROWING A BOOK
    def borrow_book(self, title):
        book = self.get_book(title)

        if book is None:
            return

        if book.available == 'No':
            print("\nAlready borrowed.")
            return

        book.available = 'No'
        print("\nBook borrowed successfully.")
#-------------------------------------------------------------
    #=== RETURNING BORROWED BOOK
    def return_book(self, title):
        book = self.get_book(title)

        if book is None:
            return

        if book.available == 'Yes':
            print("\nBook already present.")
            return

        book.available = 'Yes'
        print("\nBook returned successfully.")
#-------------------------------------------------------------