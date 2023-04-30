import uuid


class Twit:
    def __init__(self, body:str, author:str, user_id:int,id: int):
        self.body = body
        self.author = author
        self.user_id = user_id
        self.id = id