#Прослойка бизнеслогики
class ItemService:
    def __init__(self, storage):
        self.storage = storage

    def add(self, item):
        return self.storage.add(item)

    def delete(self, id):
        return self.storage.delete(id)

    def get(self):
        return self.storage.get()

    def get_by_id(self, id):
        return self.storage.get_by_id(id)

    def update(self, new_item, id):
        return self.storage.update(new_item, id)