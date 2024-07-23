import uuid
from typing import Dict


class Book:
    """Класс для представления книги в библиотеке."""

    def __init__(
        self, id: str, title: str, author: str, year: str, status: str = "в наличии"
    ):
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
            "status": self.status,
        }

    @staticmethod
    def create(title: str, author: str, year: str) -> "Book":
        """
        Создание новой книги с уникальным идентификатором.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            year (str): Год издания книги.

        Returns:
            Book: Новый объект книги.
        """
        return Book(str(uuid.uuid4()), title, author, year)
