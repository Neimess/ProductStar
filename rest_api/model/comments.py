import uuid
class comments:
    def __init__(self, body, twit_id, id):
        self.body = body
        self.id_twit = twit_id
        self.id = id
    def id_check(self):
        return self.id