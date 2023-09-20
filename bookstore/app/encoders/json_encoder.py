
from flask.json import JSONEncoder
from domain.book_db_model import SQLBook

#Преоразователь SQLBook в JSON формат
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, SQLBook):
            return {'id': obj.id,
                    "title": obj.title,
                    "publish_year": obj.publish_year,
                    'pages_count': obj.pages_count,
                    'description': obj.description,
                    'created_at': obj.created_at}
        return super().default(obj)
