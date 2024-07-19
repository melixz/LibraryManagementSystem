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


def delete_book(book_id):
    books = load_books_from_file("library.json")
    books = [book for book in books if book.id != book_id]
    save_books_to_file("library.json", books)
    print("Книга успешно удалена.")


def search_books(query, search_by):
    books = load_books_from_file("library.json")
    if search_by == "title":
        results = [book for book in books if query.lower() in book.title.lower()]
    elif search_by == "author":
        results = [book for book in books if query.lower() in book.author.lower()]
    elif search_by == "year":
        results = [book for book in books if book.year == query]
    else:
        print("Неверный параметр поиска.")
        return
    for book in results:
        print(
            f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")


def display_books():
    books = load_books_from_file("library.json")
    for book in books:
        print(
            f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")


def change_status(book_id, new_status):
    books = load_books_from_file("library.json")
    for book in books:
        if book.id == book_id:
            book.status = new_status
            save_books_to_file("library.json", books)
            print("Статус книги успешно изменен.")
            return
    print("Книга с таким ID не найдена.")


def print_menu():
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Поиск книги")
    print("4. Отображение всех книг")
    print("5. Изменение статуса книги")
    print("6. Выход")


def main():
    while True:
        print_menu()
        choice = input("Выберите действие: ")
        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            add_book(title, author, year)
        elif choice == "2":
            book_id = input("Введите ID книги для удаления: ")
            delete_book(book_id)
        elif choice == "3":
            query = input("Введите поисковый запрос: ")
            search_by = input("Искать по (title/author/year): ")
            search_books(query, search_by)
        elif choice == "4":
            display_books()
        elif choice == "5":
            book_id = input("Введите ID книги для изменения статуса: ")
            new_status = input("Введите новый статус (в наличии/выдана): ")
            change_status(book_id, new_status)
        elif choice == "6":
            break


if __name__ == "__main__":
    main()
