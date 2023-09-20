from flask import g

from application.book_service import BookService
from storage.infra.mem_storage import MemoryStorage
from storage.infra.sqlite_storage import SQLiteStorage

class Context:
    def __init__(self, app):
        book_storage = SQLiteStorage(app)
        self.book_service = BookService(book_storage)


def get_context(app):
    return app.config["CONTEXT"]