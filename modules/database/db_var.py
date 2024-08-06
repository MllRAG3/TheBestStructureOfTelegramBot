from peewee import SqliteDatabase
from config import database_name
from typing import Final

db: Final[SqliteDatabase] = SqliteDatabase(database_name)
