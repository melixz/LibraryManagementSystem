from typing import List
from library.book import Book
from library.file_handler import load_books_from_file, save_books_to_file


def add_book(
    title: str, author: str, year: str, filename: str = "library.json"
) -> None:
    """
    Добавление книги в библиотеку.

    Args:
        title (str): Название книги.
        author (str): Автор книги.
        year (str): Год издания книги.
        filename (str): Имя файла для сохранения данных. По умолчанию "library.json".
    """
    books = load_books_from_file(filename)
    new_book = Book.create(title, author, year)
    books.append(new_book)
    save_books_to_file(filename, books)
    print("Книга успешно добавлена.")


def delete_book(book_id: str, filename: str = "library.json") -> None:
    """
    Удаление книги из библиотеки по ID.

    Args:
        book_id (str): Уникальный идентификатор книги.
        filename (str): Имя файла для сохранения данных. По умолчанию "library.json".
    """
    books = load_books_from_file(filename)
    if not any(book.id == book_id for book in books):
        print("Книга с таким ID не найдена.")
        return
    books = [book for book in books if book.id != book_id]
    save_books_to_file(filename, books)
    print("Книга успешно удалена.")


def search_books(
    query: str, search_by: str, filename: str = "library.json"
) -> List[Book]:
    """
    Поиск книг в библиотеке.

    Args:
        query (str): Поисковый запрос.
        search_by (str): Поле для поиска (название, автор, год издания).
        filename (str): Имя файла для сохранения данных. По умолчанию "library.json".

    Returns:
        list: Список найденных книг.
    """
    books = load_books_from_file(filename)
    if search_by == "название":
        results = [book for book in books if query.lower() in book.title.lower()]
    elif search_by == "автор":
        results = [book for book in books if query.lower() in book.author.lower()]
    elif search_by == "год издания":
        results = [book for book in books if book.year == query]
    else:
        print("Неверный параметр поиска.")
        return []
    if not results:
        print("Книги не найдены.")
    for book in results:
        print(
            f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}"
        )
    return results


def display_books(filename: str = "library.json") -> None:
    """
    Отображение всех книг в библиотеке.

    Args:
        filename (str): Имя файла для сохранения данных. По умолчанию "library.json".
    """
    books = load_books_from_file(filename)
    if not books:
        print("Библиотека пуста.")
    for book in books:
        print(
            f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}"
        )


def change_status(
    book_id: str, new_status: str, filename: str = "library.json"
) -> None:
    """
    Изменение статуса книги в библиотеке.

    Args:
        book_id (str): Уникальный идентификатор книги.
        new_status (str): Новый статус книги ("в наличии" или "выдана").
        filename (str): Имя файла для сохранения данных. По умолчанию "library.json".
    """
    books = load_books_from_file(filename)
    for book in books:
        if book.id == book_id:
            book.status = new_status
            save_books_to_file(filename, books)
            print("Статус книги успешно изменен.")
            return
    print("Книга с таким ID не найдена.")
