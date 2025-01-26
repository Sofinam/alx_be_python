class Book:
    def __init__(self, title: str, author: str):
        """
        Base class for a book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        String representation of a Book instance.
        """
        return f"'{self.title}' by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """
        Derived class representing an eBook.
        """
        super().__init__(title, author)
        self.file_size = file_size  # File size in MB

    def __str__(self):
        """
        String representation of an EBook instance.
        """
        return f"{super().__str__()} [EBook, File size: {self.file_size}MB]"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """
        Derived class representing a printed book.
        """
        super().__init__(title, author)
        self.page_count = page_count  # Page count of the book

    def __str__(self):
        """
        String representation of a PrintBook instance.
        """
        return f"{super().__str__()} [Print Book, Pages: {self.page_count}]"


class Library:
    def __init__(self):
        """
        Class representing a library, which manages a collection of books.
        """
        self.books = []  # List to store books

    def add_book(self, book: Book):
        """
        Adds a book to the library's collection.
        """
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Error: Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        """
        Lists all the books in the library.
        """
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book}")
