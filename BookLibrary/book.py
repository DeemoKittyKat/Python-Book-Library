class Book:

    bid = 0
    
    def __init__(self, name, author, category, rating):
        self.name = name
        self.author = author
        self.category = category
        self.rating = rating
        Book.bid += 1
        self.book_id = Book.bid

        # Increase the static book id

    def show_info(self):
        print("""
Title: {0}
Author: {1}
Category: {2}
Rating: {3}
Book ID: {4}
        """.format(self.name, self.author, self.category, self.rating, self.book_id))