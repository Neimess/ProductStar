
class User:

    def __init__(self, username: str, id: int):
        self.username = username
        self.id = id
    def get_id(self):
        return self.id