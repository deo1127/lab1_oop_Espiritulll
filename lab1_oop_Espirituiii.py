#DEOLOSIS KARL ESPIRITU III
#BSIS 2B
class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Welcome to {self.name}!")
        print()

# ---------- Car ----------
class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand  = brand
        self.model  = model
        self.year   = year
        self.odometer = 0

    def drive(self, km):
        if km < 0:
            print(f"Invalid! Cannot drive negative km: {km}")
        else:
            self.odometer += km
            print(f"{self.brand:<6} {self.model:<8} drove {km:>3} km. Odometer: {self.odometer:>3} km")

    def age(self, current_year):
        return current_year - self.year

    def __str__(self):
        return f"{self.year} {self.brand:<6} {self.model:<8} - {self.odometer:>3} km, {self.wheels} wheels"

# ---------- Book ----------
class Book:
    total_books = 0

    def __init__(self, title, author, copies):
        self.title     = title
        self.author    = author
        self.copies    = copies
        self.available = copies
        Book.total_books += 1

    def borrow(self):
        if self.available > 0:
            self.available -= 1
            print(f"Borrowed '{self.title}'. Available now: {self.available}")
        else:
            print(f"Sorry, '{self.title}' is not available.")

    def return_book(self):
        if self.available < self.copies:
            self.available += 1
            print(f"Returned '{self.title}'. Available now: {self.available}")
        else:
            print(f"All copies of '{self.title}' are already returned.")

    def __str__(self):
        return f"'{self.title:<6}' by {self.author:<8} - {self.available}/{self.copies} available"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.copies})"

# ---------- RUN ----------

greeter = Greeter("you")
greeter.greet()

print("Garage")
car1 = Car("Mazda", "3",       2023)
car2 = Car("Honda", "CR-V",    2025)
car3 = Car("Jeep",  "Wrangler", 2017)
print(car1)
print(car2)
print(car3)
print(f"All cars have {Car.wheels} wheels")
print()

print("On the Road")
car1.drive(50)
car2.drive(120)
car3.drive(30)
print(f"{car1.brand:<6} {car1.model:<8} age: {car1.age(2026)}")
print(f"{car2.brand:<6} {car2.model:<8} age: {car2.age(2026)}")
print(f"{car3.brand:<6} {car3.model:<8} age: {car3.age(2026)}")
print(car1)
print(car2)
print(car3)
print()

print("Library")
book1 = Book("Book 1", "Author 1", 3)
book2 = Book("Book 2", "Author 2", 2)
print(book1)
print(book2)
print(f"Total books: {Book.total_books}")
print([book1, book2])
book1.borrow()
book1.borrow()
book1.borrow()
book1.borrow()
book1.return_book()
print(book1)

# ---------- Reflection ----------
"""
1. Class vs Object:
   Class is the blueprint, like Car. Object is the real thing, like car1 = Car("Mazda", "3", 2023).

2. What is self?
   self is the specific object calling the method.
   It lets Python know which car's odometer or which Greeter's name to use.

3. Class attribute vs Instance attribute:
   Class attribute is shared by ALL, like wheels = 4 and total_books = 0.
   Instance attribute is unique to ONE, like self.brand, self.title, self.name.

4. Real-world design:
   I would design a Student class for a school system.
   Instance attributes: name, student_id, grade.
   Class attribute: school_name.
   Methods: enroll(), drop_subject(), get_gpa().
"""
