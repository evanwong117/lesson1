class Book:
    def __init__(self, name, author):
        self.title = self.title
        self.author = author
        self.is_borrowed = False
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed - True
            print(f"Success: You have borrowed '{self.title}'.")
        else:
            print(f"Sorry: '{self.title}' is already borrowed.")
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"Success: '{self.title}' has been returned.")
        else:
            print(f"Notice: '{self.title}' was not checked out.")
book1 = Book("Project Hail Mary", "Andy Weir")
book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")
book3 = Book("Lord of the Rings", "J.R.R. Tolkien")
print("--- Borrowing Demonstration ---")
book1.borrow()
book2.borrow()
book1.borrow()
print("\n--- Returning Demonstration ---")
book1.return_book()
book3.return_book()