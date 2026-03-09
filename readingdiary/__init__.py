from datetime import datetime

class Note:

    def __init__(self, text, page, date):
        self.text = text
        self.page = page
        self.date = date

    def __str__(self):
        return f"{self.date} - page {self.page}: {self.text}"


class Book:
    EXCELLENT = 3
    GOOD = 2
    BAD = 1
    UNRATED = -1

    def __init__(self, isbn, title, author, pages):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.pages = pages
        self.rating = Book.UNRATED
        self.notes = []

    def add_note(self, text, page, date):
        if page > self.pages:
            return False

        note = Note(text, page, date)
        self.notes.append(note)
        return True

    def set_rating(self, rating):
        if rating not in (Book.EXCELLENT, Book.GOOD, Book.BAD):
            return False

        self.rating = rating
        return True

    def get_notes_of_page(self, page):
        notes_page = []