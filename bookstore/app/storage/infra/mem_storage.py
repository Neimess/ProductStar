from abc import abstractmethod
from domain.book import Book


class MemoryStorage:
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def get_by_id(self):
        pass


class LocalStorage(MemoryStorage):
    def __init__(self):
        self.books = {}

    def add(self, book: Book):
        id = len(self.books)
        self.books[id] = book
        return id

    def delete(self, id):
        if self.books.get(id) is not None:
            del self.books[id]
        return {
            "ResponseText": "Such ID doesn't exist",
            "Response": 400
        }

    def get(self):
        return self.books

    def get_by_id(self, id):
        return self.books.get(id)
    
    def update(self, book: Book, id):
        if self.books.get(id) is not None:
            self.books[id] = book
            return {
                "ResponseText": "OK",
                "Response": 200
            }
        return {
            "ResponseText": "Such ID doesn't exist",
            "Response": 400
        }
