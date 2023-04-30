
class Comment:
    def __init__(self, body:str, twit_id:int, id:int):
        self.body = body
        self.twit_id = twit_id
        self.id = id
    def get_id(self):
        return self.id
    def get_twit_id(self):
        return self.twit_id