class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True  

class Library:
    def __init__(self):
        self.books = []
        self.students = {} 

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"{title} added successfully.")

    def display_books(self):
        print("\n--- Library Catalog ---")
        if not self.books:
            print("The library is empty.")
            return
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"'{book.title}' by {book.author} [{status}]")

class Student:
    def __init__(self, name, student_id, has_membership=True):
        self.name = name
        self.student_id = student_id
        self.has_membership = has_membership
        self.borrowed_books = []  

    def display_profile(self):
        status = "Active" if self.has_membership else "No Membership"
        books_held = ','.join([book.title for book in self.borrowed_books])
        print(f"\n Student: {self.name} | ID: {self.student_id} | Membership: {status}")
        print(f"Borrowed Books: {', '.join(books_held) if books_held else 'None'}")

class Librarian:
    def __init__(self, name):
        self.name = name

    def check_eligibility(self, student):
        if not student.has_membership:
            print(f"Access Denied: {student.name} does not have an active membership.")
            return False
        return True

    def process_borrow(self, library, student_id, title):
        student = library.students.get(student_id)
        if not student:
            print("Student profile not found.")
            return

        if not self.check_eligibility(student):
            return

        for book in library.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.is_available = False
                    student.borrowed_books.append(book)
                    print(f"Librarian {self.name} authorized: '{book.title}' borrowed by {student.name}.")
                    return
                else:
                    print(f"{book.title} is already borrowed.")
                    return
        print("Book not found in catalog.")

    def process_return(self, library, student_id, title):
        student = library.students.get(student_id)
        if not student:
            print("Student profile not found.")
            return

        for book in student.borrowed_books:
            if book.title.lower() == title.lower():
                book.is_available = True
                student.borrowed_books.remove(book)
                print(f"Librarian {self.name} processed return: '{book.title}' from {student.name}.")
                return
        print(f"This student does not have '{title}' on their record.")

library = Library()
librarian = Librarian("Name")

library.add_book("The Hobbit", "J.R.R. Tolkien")
library.add_book("1984", "George Orwell")

library.students["S101"] = Student("John Doe", "S101", has_membership=True)
library.students["S102"] = Student("Jane Smith", "S102", has_membership=False)

while True:
    print("\nMenu: 1. View Catalog | 2. Add Book | 3. Borrow Book | 4. Return Book | 5. View Student Info | 6. Exit")
    choice = input("Enter choice (1-6): ")
    
    if choice == "1":
        library.display_books()
    elif choice == "2":
        t = input("Enter Book Title: ")
        a = input("Enter Book Author: ")
        library.add_book(t, a)
    elif choice == "3":
        s_id = input("Enter Student ID: ")
        t = input("Enter Title to Borrow: ")
        librarian.process_borrow(library, s_id, t)
    elif choice == "4":
        s_id = input("Enter Student ID: ")
        t = input("Enter Title to Return: ")
        librarian.process_return(library, s_id, t)
    elif choice == "5":
        s_id = input("Enter Student ID: ")
        student = library.students.get(s_id)
        if student:
            student.display_profile()
        else:
            print("Student not found.")
    elif choice == "6":
        print("Thank you for visiting")
        break
    else:
        print("Invalid choice. Please pick 1 to 6.")
