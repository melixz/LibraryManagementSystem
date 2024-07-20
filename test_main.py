import uuid
import unittest
from main import Book, add_book, delete_book, search_books, change_status, load_books_from_file, \
    save_books_to_file


class TestLibraryManagementSystem(unittest.TestCase):

    def setUp(self):
        self.test_books = [
            Book(str(uuid.uuid4()), "Test Book 1", "Author 1", "2001"),
            Book(str(uuid.uuid4()), "Test Book 2", "Author 2", "2002"),
            Book(str(uuid.uuid4()), "Test Book 3", "Author 3", "2003")
        ]
        save_books_to_file("test_library.json", self.test_books)

    def tearDown(self):
        import os
        os.remove("test_library.json")

    def test_add_book(self):
        add_book("New Book", "New Author", "2024", "test_library.json")
        books = load_books_from_file("test_library.json")
        self.assertEqual(len(books), 4)
        self.assertEqual(books[-1].title, "New Book")

    def test_delete_book(self):
        book_id = self.test_books[0].id
        delete_book(book_id, "test_library.json")
        books = load_books_from_file("test_library.json")
        self.assertEqual(len(books), 2)
        self.assertNotIn(book_id, [book.id for book in books])

    def test_search_books_by_title(self):
        results = search_books("Test Book 1", "название", "test_library.json")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Test Book 1")

    def test_search_books_by_author(self):
        results = search_books("Author 2", "автор", "test_library.json")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].author, "Author 2")

    def test_search_books_by_year(self):
        results = search_books("2003", "год издания", "test_library.json")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].year, "2003")

    def test_change_status(self):
        book_id = self.test_books[0].id
        change_status(book_id, "выдана", "test_library.json")
        books = load_books_from_file("test_library.json")
        self.assertEqual(books[0].status, "выдана")


if __name__ == "__main__":
    unittest.main()
