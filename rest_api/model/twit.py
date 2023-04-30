
class Twit:
    def __init__(self, body:str, author:str, user_id:int, id:int):
        self.body = body
        self.author = author
        self.user_id = user_id
        self.id = id
        
    def get_id(self):
        return self.id
    def get_user_id(self):
        return self.user_id