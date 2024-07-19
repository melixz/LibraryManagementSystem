import json
import uuid


class Book:
    def __init__(self, id, title, author, year, status="available"):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    def load_books_from_file(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                books_data = json.load(file)
                return [Book(**data) for data in books_data]
        except FileNotFoundError:
            return []

    def save_books_to_file(filename, books):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in books], file, ensure_ascii=False, indent=4)

    def add_book(title, author, year):
        books = load_books_from_file("library.json")
        book_id = str(uuid.uuid4())
        new_book = Book(book_id, title, author, year)
        books.append(new_book)
        save_books_to_file("library.json", books)
        print("Книга успешно добавлена.")
