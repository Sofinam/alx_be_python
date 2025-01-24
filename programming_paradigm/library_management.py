def __init__(self, title, author):
    self.title = title
    self.author = author
    self._is_checked_out = False

def check_out(self):
    """Mark the book as checked out."""
    if not self._is_checked_out:
        self._is_checked_out = True
        return True
    return False

def return_book(self):
    """Mark the book as available."""
    if self._is_checked_out:
        self._is_checked_out = False
        return True
    return False

def is_available(self):
    """Check if the book is available."""
    return not self._is_checked_out

class Library:
    """A classs representing a library that manages a collection of books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f" '{title}' has been checked out.")
                    return
        print(f" '{title}' is not availaible for checkout.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f" '{title}' has been returned.")
                    return
        print(f"'{title}' is not currently checked out.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")        

