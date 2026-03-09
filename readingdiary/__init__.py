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

        for note in self.notes:
            if note.page == page:
                notes_page.append(note)

        return notes_page

    def page_with_most_notes(self):
        if not self.notes:
            return -1

        count_pages = {}

        for note in self.notes:
            if note.page not in count_pages:
                count_pages[note.page] = 0
            count_pages[note.page] += 1

            max_page = -1
            max_notes = 0

            for page, count in count_pages.items():
                if count > max_notes:
                    max_notes = count
                    max_page = page

            return max_page

    def __str__(self):
        if self.rating == Book.EXCELLENT:
            rating_str = "excellent"
        elif self.rating == Book.GOOD:
            rating_str = "good"
        elif self.rating == Book.BAD:
            rating_str = "bad"
        else:
            rating_str = "unrated"

        return (
            f"ISBN: {self.isbn}\n"
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Pages: {self.pages}\n"
            f"Rating: {rating_str}"
        )