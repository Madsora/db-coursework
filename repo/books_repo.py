from repo.base_repo import BaseRepository
from db.connection import db

books_repo = BaseRepository(db['books'])