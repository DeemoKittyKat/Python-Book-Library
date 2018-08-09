from library import Library
from book import Book

import sys

class Menu:

    def __init__(self):
        self.lib = Library()
        self.selected_book = Book("","","","")
        self.options = {
            "1": self.add_book,
            "2": self.display_all,
            "3": self.display_current,
            "4": self.select_book,
            "5": self.deselect_book,
            "6": self.search,
            "7": self.modify_selected,
            "99": self.display_menu,
            "0": self.exit
        }
        self.test_case()

    def test_case(self):
        self.lib.add_book("Peter", "Robinson", "Action", "5")
        self.lib.add_book("John Doe", "Peter Jake", "Adventure", "3")
        self.lib.add_book("Orange John", "LoL", "Action", "3")

    #method get_input()
    def get_input(self):
        return raw_input("> ")

    #method display_menu()
    def display_menu(self):
        print("""
Welcome to your digital console library!
Please type one of the following:

1. Add a new book
2. Display all read books
3. Display currently selected book
4. Select a book using an ID
5. Deselect currently selected book
6. Search for specific books
7. Modify selected book


99. Display these options
0. Exit
        """)

    #method display_search_options()
    def display_search(self):
        print("""
How would you like to search for your book?:

1. By name
2. By author
3. By category
4. By rating
5. By id

0. Exit
        """)

    #method beautify(func)
    def beautify(self, func):
        print("*=========*")
        func()
        print("*=========*")

    #method run()
    def run(self):
        self.beautify(self.display_menu)

        is_running = True

        while is_running:
            option = str(self.get_input())
            action = self.options.get(option)
            if action != None:
                action()
            else:
                print("\"{0}\" is not a valid option. Please try again")

    #method add_book()
    def add_book(self):
        print("""
To add a book, type \"name, author, category, rating\"
To quit, type \"0\"
        """)
        is_adding = True
        while is_adding:
            param_arr = str(self.get_input()).strip().split(",")
            if len(param_arr) == 4:
                self.lib.add_book(param_arr[0],param_arr[1],param_arr[2],param_arr[3])
                print("Book \"{0}\" was added!".format(param_arr[0]))
            elif len(param_arr) == 1:
                if param_arr[0] == "0":
                    print("Exiting...")
                    is_adding = False
                else:
                    print("Invalid parameters were given.")
            else:
                print("Not enough parameters were given.")
    #method display_all()
    def display_all(self):
        if len(self.lib.books) > 0:
            for b in self.lib.books:
                self.beautify(b.show_info)
        else:
            print("Currently, you have no books read.")
    #method display_current()
    def display_current(self):
        if self.selected_book != None:
            self.beautify(self.selected_book.show_info)
        else:
            print("No book has been selected.")
    #method select_book()
    def select_book(self):
        is_selecting = True

        while is_selecting:
            print("""
Please enter an ID of a book you wish to select!
Type \"-1\" to leave.
            """)
            try:
                b_id = int(self.get_input())
                if b_id != "-1":
                    book_arr = self.lib.search(book_id=b_id)
                    if len(book_arr) == 1:
                        self.selected_book = book_arr[0]
                    
                    if self.selected_book == None:
                        print("No book was selected")
                    else:
                        print("Selected book...")   
                        self.beautify(self.selected_book.show_info)

                print("Exiting...")
                is_selecting = False
            except ValueError:
                print("\"{0}\" was not a valid ID. Please try again.".format(b_id))
    #method deselect_book()
    def deselect_book(self):
        if self.selected_book != None:
            self.selected_book = None
            print("\"{0}\" book has been deselected".format(self.selected_book.name))
        else:
            print("No book was currently selected")
    #method search()
    def search(self):
        self.beautify(self.display_search)

        is_searching = True
        
        while is_searching:
            try:
                option = int(self.get_input())
                name = author = category = rating = b_id = None
                if option == 1:
                    print("Please enter a name.")
                    name = str(self.get_input())
                elif option == 2:
                    print("Please enter an author.")
                    author = str(self.get_input())
                elif option == 3:
                    print("Please enter a category.")
                    category = str(self.get_input())
                elif option == 4:
                    print("Please enter a rating.")
                    rating = str(self.get_input())
                elif option == 5:
                    print("Please enter an ID.")
                    b_id = str(self.get_input())
                elif option == 0:
                    print("Exiting search...")
                    is_searching = False
                else:
                    raise ValueError("\"{0}\" was not a valid option!".format(option))

                book_arr = self.lib.search(name=name, author=author, category=category, rating=rating, book_id=b_id)
                if len(book_arr) > 0:
                    for b in book_arr:
                        self.beautify(b.show_info)
                else:
                    print("You have currently no books read. Keep reading!")
                
                is_searching = False
            except ValueError as error:
                print(repr(error))

    #method modify_selected()
    def modify_selected(self):
        if self.selected_book != None:
            is_modifying = True
            print("""
To modify a book, type \"name, author, category, rating\"
If there's a parameter you wish to not edit, type \"none\" to keep it
To exit, type \"0\"
            """)
            while is_modifying:
                param_arr = str(self.get_input()).split(",")
                if len(param_arr) == 4:
                    self.lib.modify_book(param_arr[0],param_arr[1],param_arr[2],param_arr[3])
                elif len(param_arr) == 1:
                    print("Exiting...")
                    is_modifying = False
                else:
                    print("Not enough parameters were passed.")
        else:
            print("No book was selected for modification.")
    #methods exit()
    def exit(self):
        print("Keep on reading!")
        sys.exit(0)

if __name__ == "__main__":
    menu = Menu()
    menu.run()