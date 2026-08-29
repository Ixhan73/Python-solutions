from library_classes import Book
import json

def save_books(library):
    books = []

    for book in library.books:
        books.append({
            "Title": book.title,
            "Author": book.author,
            "Available": book.available,
        })

    with open('library.json', 'w') as file:
        json.dump(books, file, indent=4)

def load_books():
    try:
        with open('library.json', 'r') as file:
            data = json.load(file)

            books = []
            for book in data:
                books.append(
                    Book(
                        book["Title"],
                        book["Author"],
                        book["Available"]
                    )
                )

            return books

    except (FileNotFoundError, json.JSONDecodeError):
        return []