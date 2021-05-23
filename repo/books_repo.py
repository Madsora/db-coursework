import numpy as np
from repo.base_repo import BaseRepository
from db.connection import db
from repo.authors_repo import authors_repo


class BooksRepository(BaseRepository):
    def __init__(self, collection):
        super().__init__(collection)

    def find_books_by_author(self, author_name):
        author = authors_repo.find_author_by_name(author_name)
        for a in author:
            books = self.find({'author_id': a['_id']})
        return books

books_repo = BooksRepository(db['books'])