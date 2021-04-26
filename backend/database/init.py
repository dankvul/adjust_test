import sqlalchemy
import databases

from config import DATABASE_URL


__all__ = ["db"]


class SQLAlchemy:
    def __init__(self):
        self._database = databases.Database(DATABASE_URL)
        self._metadata = sqlalchemy.MetaData()

    @property
    def metadata(self):
        return self._metadata

    @property
    def database(self):
        return self._database


db = SQLAlchemy()
