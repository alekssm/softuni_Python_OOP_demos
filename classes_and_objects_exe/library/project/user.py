from library import Library


class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library: Library):
        for u, b in library.rented_books.items():
            if book_name in b:
                return f'The book "{book_name}" is already rented and will be available in\
                 {b[book_name]} days!'
        for a, b in library.books_available:
            if book_name in b:
