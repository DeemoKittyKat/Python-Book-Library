from book import Book

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, name, author, category, rating):
        self.books.append(Book(name, author, category, rating))

    # for now only works with one of the options at a time
    def search(self, name=None, author=None, category=None, rating=None, book_id=None):
        book_arr = []
        for book in self.books:
            if book.name == name:
                book_arr.append(book)
            elif book.author == author:
                book_arr.append(book)
            elif book.category == category:
                book_arr.append(book)
            elif book.rating == rating:
                book_arr.append(book)
            elif book.book_id == book_id:
                book_arr.append(book)
        return book_arr

    def modify_book(self, book, name=None, author=None, category=None, rating=None):
        for b in self.books:
            if b is book:
                if name and name.lower() != "none":
                    book.name = b.name = name
                if author and author.lower() != "none":
                    book.author = b.author = author
                if category and category.lower() != "none":
                    book.category = b.category = category
                if rating and rating.lower() != "none":
                    book.rating = b.rating = rating
                break

    