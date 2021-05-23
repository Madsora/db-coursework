import numpy as np
from repo.base_repo import BaseRepository
from db.connection import db
class AuthorsRepository(BaseRepository):
    def __init__(self, collection):
        super().__init__(collection)

    def find_author_by_name(self, name):
        author = self.find({'name': name})
        return author

authors_repo = AuthorsRepository(db['authors'])