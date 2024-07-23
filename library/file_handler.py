import json
from typing import List
from library.book import Book
from library.exceptions import FileProcessingError


def load_books_from_file(filename: str) -> List[Book]:
    """
    Загрузка книг из файла.

    Args:
        filename (str): Имя файла для загрузки данных.

    Returns:
        list: Список объектов Book.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            if not content:
                return []
            books_data = json.loads(content)
            return [Book(**data) for data in books_data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        raise FileProcessingError(filename)


def save_books_to_file(filename: str, books: List[Book]) -> None:
    """
    Сохранение книг в файл.

    Args:
        filename (str): Имя файла для сохранения данных.
        books (list): Список объектов Book для сохранения.
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(
                [book.to_dict() for book in books], file, ensure_ascii=False, indent=4
            )
    except Exception:
        raise FileProcessingError(filename)
