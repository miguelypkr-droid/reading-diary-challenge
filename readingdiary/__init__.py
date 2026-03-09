from datetime import datetime

class Note:

    def __init__(self, text, page, date):
        self.text = text
        self.page = page
        self.date = date

    def __str__(self):
        return f"{self.date} - page {self.page}: {self.text}"


class Book: