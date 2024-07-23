from library.library import (
    add_book,
    delete_book,
    search_books,
    display_books,
    change_status,
)
from library.exceptions import (
    BookNotFoundError,
    InvalidSearchParameterError,
    FileProcessingError,
)


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


def print_search_menu() -> None:
    """
    Отображение меню поиска для пользователя.
    """
    print("1. Искать по названию")
    print("2. Искать по автору")
    print("3. Искать по году издания")


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
            try:
                add_book(title, author, year)
            except FileProcessingError as e:
                print(e)
        elif choice == "2":
            book_id = input("Введите ID книги для удаления: ")
            try:
                delete_book(book_id)
            except BookNotFoundError as e:
                print(e)
            except FileProcessingError as e:
                print(e)
        elif choice == "3":
            print_search_menu()
            search_choice = input("Выберите категорию поиска: ")
            if search_choice == "1":
                search_by = "название"
            elif search_choice == "2":
                search_by = "автор"
            elif search_choice == "3":
                search_by = "год издания"
            else:
                print("Неверный выбор. Пожалуйста, выберите категорию от 1 до 3.")
                continue
            query = input("Введите поисковый запрос: ")
            try:
                search_books(query, search_by)
            except InvalidSearchParameterError as e:
                print(e)
            except FileProcessingError as e:
                print(e)
        elif choice == "4":
            try:
                display_books()
            except FileProcessingError as e:
                print(e)
        elif choice == "5":
            book_id = input("Введите ID книги для изменения статуса: ")
            new_status = input("Введите новый статус (в наличии/выдана): ")
            try:
                change_status(book_id, new_status)
            except BookNotFoundError as e:
                print(e)
            except FileProcessingError as e:
                print(e)
        elif choice == "6":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 6.")


if __name__ == "__main__":
    main()
