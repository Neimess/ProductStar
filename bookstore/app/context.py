from flask import g

from application.book_service import ItemService
from storage.infra.mem_storage import LocalStorage
from storage.infra.sqlite_storage import DataBaseStorage

class Context:
    def __init__(self, app):
        book_storage = DataBaseStorage(app)
        # book_storage = LocalStorage()
        self.book_service = ItemService(book_storage)


def get_context(app):
    return app.config["CONTEXT"]