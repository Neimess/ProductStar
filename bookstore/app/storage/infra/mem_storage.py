from abc import abstractmethod
from domain.book import Book
from uuid import uuid1



class MemoryStorage:
    @abstractmethod
    def add(self):
        pass

    def update(self):
        pass
    
    def delete(self, id):
        pass

    def get(self):
        pass


class LocalStorage(MemoryStorage):
    def __init__(self):
        self.books = {}

    def add(self, book: Book):
        id = uuid1()
        self.books[id] = book
        return id

    def delete(self, id):
        del self.books[id]

    def get(self):
        return self.books


