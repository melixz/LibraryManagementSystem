import uuid
import json
from typing import List, Dict


class Book:
    """Класс для представления книги в библиотеке."""

    def __init__(self, id: str, title: str, author: str, year: str, status: str = "в наличии"):
        """
        Инициализация книги.

        Args:
            id (str): Уникальный идентификатор книги.
            title (str): Название книги.
            author (str): Автор книги.
            year (str): Год издания книги.
            status (str): Статус книги. По умолчанию "в наличии".
        """
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> Dict[str, str]:
        """
        Преобразование объекта книги в словарь.

        Returns:
            dict: Словарь с данными книги.
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }


def load_books_from_file(filename: str) -> List[Book]:
    """
    Загрузка книг из файла.

    Args:
        filename (str): Имя файла для загрузки данных.

    Returns:
        list: Список объектов Book.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content:  # Если файл пуст
                return []
            books_data = json.loads(content)
            return [Book(**data) for data in books_data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Ошибка при чтении файла {filename}. Файл может быть поврежден.")
        return []


def save_books_to_file(filename: str, books: List[Book]) -> None:
    """
    Сохранение книг в файл.

    Args:
        filename (str): Имя файла для сохранения данных.
        books (list): Список объектов Book для сохранения.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump([book.to_dict() for book in books], file, ensure_ascii=False, indent=4)


def add_book(title: str, author: str, year: str) -> None:
    """
    Добавление книги в библиотеку.

    Args:
        title (str): Название книги.
        author (str): Автор книги.
        year (str): Год издания книги.
    """
    try:
        books = load_books_from_file("library.json")
        book_id = str(uuid.uuid4())
        new_book = Book(book_id, title, author, year)
        books.append(new_book)
        save_books_to_file("library.json", books)
        print("Книга успешно добавлена.")
    except Exception as e:
        print(f"Ошибка при добавлении книги: {e}")


def delete_book(book_id: str) -> None:
    """
    Удаление книги из библиотеки по ID.

    Args:
        book_id (str): Уникальный идентификатор книги.
    """
    try:
        books = load_books_from_file("library.json")
        if not any(book.id == book_id for book in books):
            print("Книга с таким ID не найдена.")
            return
        books = [book for book in books if book.id != book_id]
        save_books_to_file("library.json", books)
        print("Книга успешно удалена.")
    except Exception as e:
        print(f"Ошибка при удалении книги: {e}")


def search_books(query: str, search_by: str) -> List[Book]:
    """
    Поиск книг в библиотеке.

    Args:
        query (str): Поисковый запрос.
        search_by (str): Поле для поиска (title, author, year).

    Returns:
        list: Список найденных книг.
    """
    try:
        books = load_books_from_file("library.json")
        if search_by == "title":
            results = [book for book in books if query.lower() in book.title.lower()]
        elif search_by == "author":
            results = [book for book in books if query.lower() in book.author.lower()]
        elif search_by == "year":
            results = [book for book in books if book.year == query]
        else:
            print("Неверный параметр поиска.")
            return []
        for book in results:
            print(
                f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")
        return results
    except Exception as e:
        print(f"Ошибка при поиске книг: {e}")
        return []


def display_books() -> None:
    """
    Отображение всех книг в библиотеке.
    """
    try:
        books = load_books_from_file("library.json")
        if not books:
            print("Библиотека пуста.")
        for book in books:
            print(
                f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")
    except Exception as e:
        print(f"Ошибка при отображении книг: {e}")


def change_status(book_id: str, new_status: str) -> None:
    """
    Изменение статуса книги в библиотеке.

    Args:
        book_id (str): Уникальный идентификатор книги.
        new_status (str): Новый статус книги ("в наличии" или "выдана").
    """
    try:
        books = load_books_from_file("library.json")
        for book in books:
            if book.id == book_id:
                book.status = new_status
                save_books_to_file("library.json", books)
                print("Статус книги успешно изменен.")
                return
        print("Книга с таким ID не найдена.")
    except Exception as e:
        print(f"Ошибка при изменении статуса книги: {e}")


def print_menu() -> None:
    """
    Отображение меню для пользователя.
    """
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Поиск книги")
    print("4. Отображение всех книг")
    print("5. Изменение статуса книги")
    print("6. Выход")


def main() -> None:
    """
    Главная функция, запускающая приложение.
    """
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
        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 6.")


if __name__ == "__main__":
    main()
