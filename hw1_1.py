from abc import ABC, abstractmethod
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO)


# Принцип єдиної відповідальності (SRP): окремий клас для зберігання інформації про книгу
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title: str = title
        self.author: str = author
        self.year: int = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# Принцип розділення інтерфейсів (ISP) та інверсії залежностей (DIP)
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


# Принцип відкритості/закритості (OCP): можливість розширення без зміни існуючого коду
class Library(LibraryInterface):
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logging.info(f"Book added: {book}")

    def remove_book(self, title: str) -> None:
        self.books = [book for book in self.books if book.title != title]
        logging.info(f"Book removed: {title}")

    def show_books(self) -> None:
        for book in self.books:
            logging.info(book)


# Принцип інверсії залежностей (DIP): LibraryManager залежить від абстракції, а не конкретного класу Library
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library: LibraryInterface = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()


# Основна функція для взаємодії з користувачем
def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command: str = (
            input("Enter command (add, remove, show, exit): ").strip().lower()
        )

        match command:
            case "add":
                title: str = input("Enter book title: ").strip()
                author: str = input("Enter book author: ").strip()
                year: int = int(input("Enter book year: ").strip())
                manager.add_book(title, author, year)
            case "remove":
                title: str = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logging.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
