class BookNotFoundError(Exception):
    """Исключение, выбрасываемое, когда книга не найдена."""

    def __init__(self, book_id: str):
        self.book_id = book_id
        super().__init__(f"Книга с ID {book_id} не найдена.")


class InvalidSearchParameterError(Exception):
    """Исключение, выбрасываемое при неверном параметре поиска."""

    def __init__(self, parameter: str):
        self.parameter = parameter
        super().__init__(f"Неверный параметр поиска: {parameter}")


class FileProcessingError(Exception):
    """Исключение, выбрасываемое при ошибке обработки файла."""

    def __init__(self, filename: str):
        self.filename = filename
        super().__init__(f"Ошибка при обработке файла: {filename}")
