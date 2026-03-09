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
