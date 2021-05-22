
from repo.base_repo import BaseRepository
from db.connection import db

authors_repo = BaseRepository(db['authors'])