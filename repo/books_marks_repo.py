import numpy as np
from repo.base_repo import BaseRepository
from db.connection import db
from repo.books_repo import books_repo


class BooksMarksRepository(BaseRepository):
    def __init__(self, collection):
        super().__init__(collection)

    def get_book_marks(self, book_id):
        marks = []
        books = books_repo.find({'_id': book_id})

        for b in books:
            book_marks = self.find({'book_id': b['_id']})
            marks = np.append(marks, book_marks)
        return marks

books_marks_repo = BooksMarksRepository(db['books_marks'])