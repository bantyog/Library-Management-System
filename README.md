# Library Management System (LMS)

## Project Overview

This project is a Python-based implementation of a Library Management System. It serves as a **salient** [most noticeable or important] demonstration of the Software Development Life Cycle (SDLC) for a 200-level Software Engineering assignment.

---

## 1. Full SDLC Explanation

### Phase 1: Planning

The goal was to create a system to manage library assets. We identified two primary entities: **Book** and **Member**. The **Library** class acts as the central controller to **obviate** [remove/prevent] manual tracking errors.

### Phase 2: Design (Nomenclature Mapping)

To ensure technical **fidelity** [faithfulness to a detail], the design names were strictly mapped to the implementation:

| Design Entity | Attribute/Method Name | Purpose |
| --- | --- | --- |
| **Book** | `book_id`, `is_issued` | Tracks unique IDs and availability. |
| **Member** | `member_id`, `name` | Tracks user identification. |
| **Library** | `add_book()` | Method to populate the system. |
| **Library** | `register_member()` | Method to enroll new users. |
| **Library** | `issue_book()` | Logic for lending books. |

### Phase 3: Implementation

The design was translated into a **modular** [consisting of separate parts] Python script (`lms_system.py`) using Object-Oriented Programming.

### Phase 4: Testing

Unit testing was conducted to verify that `issue_book()` correctly toggles the `is_issued` boolean and prevents multiple checkouts of the same book.

### Phase 5: Deployment

The project is hosted on GitHub to allow for version control and **perpetual** [never-ending/permanent] access to the source code.

---

## 2. Implementation Code

The following names in the implementation are a **manifest** [clear/obvious] match to the design phase above.

```python
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.is_issued = False

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id

class Library:
    def add_book(self, book):
        # Implementation logic...
    
    def register_member(self, member):
        # Implementation logic...

    def issue_book(self, book_id, member_id):
        # Implementation logic...

```

---

## 3. How to Run

1. Clone the repository.
2. Run the command: `python lms_system.py`

> **Note:** This project was developed by Ogemade Folarin at Caleb University, Nigeria.

---
