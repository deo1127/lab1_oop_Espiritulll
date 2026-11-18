class Book:
    book_counter = 0  
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        Book.book_counter += 1

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Borrowed: {self.title}")
        else:
            print(f" '{self.title}' is already borrowed!")

    def return_book(self):
        if self.is_borrowed:
           self.is_borrowed = False
           print(f"Returned: {self.title}")
        else:
            print(f" '{self.title}' is not borrowed!")

    def __str__(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"'{self.title}' by {self.author} — {status}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', borrowed={self.is_borrowed})"


print("\n" + "="*50)
book1 = Book("The Giver", "Lois Rowling")
book2 = Book("The Hunger Games", "Collins, Suzanne")

print(f"Total books in library: {Book.book_counter}")
print(book1)
book1.borrow()
book1.borrow()
print(book1)
book1.return_book()
print(book1)
print("\n__repr__ output:")
print(repr(book2))