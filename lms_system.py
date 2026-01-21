class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def register_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered.")

    def issue_book(self, book_id, member_id):
        book = next((b for b in self.books if b.book_id == book_id), None)
        if book and not book.is_issued:
            book.is_issued = True
            print(f"Book {book_id} issued to Member {member_id}.")
        else:
            print("Issue failed: Book unavailable or not found.")

# Execution
lms = Library()
lms.add_book(Book("B001", "Cybersecurity Essentials", "John Doe"))
lms.register_member(Member("M001", "Student User"))
lms.issue_book("B001", "M001")
