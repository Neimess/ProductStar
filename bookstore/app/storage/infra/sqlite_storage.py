from datetime import datetime
from flask import jsonify
from .mem_storage import MemoryStorage
from domain.book_db_model import SQLBook, db
from domain.book import Book


class DataBaseStorage(MemoryStorage):
    '''
        Не понял как реализовать класс,
        не передавая в него app
    '''

    def __init__(self, app=None, database_uri="sqlite:///test.db"):

        self.database_uri = database_uri
        self.db = db
        if app is not None:

            self.__init_app__(app)

    def __init_app__(self, app):
        # Инициализация конфигурационного файла
        self.app = app
        self.app.config["SQLALCHEMY_DATABASE_URI"] = self.database_uri
        self.db.init_app(self.app)
        # Обнуление и создание базы данных
        self.db.drop_all()
        self.db.create_all()

    def add(self, item: Book):
        # Добавление объекта в БД
        db_item = SQLBook(
            title=item.title,
            publish_year=item.publish_year,
            pages_count=item.pages_count,
            description=item.description,
            created_at=datetime.strptime(item.created_at, "%Y-%m-%d")
        )
        '''
        Нужна ли проверка
        соединения, проверяющий напишите как.
        Или насколько я знаю, SQLAlchemy управляет соединением сам
        '''
        self.db.session.add(db_item)
        self.db.session.commit()
        return db_item.id

    def delete(self, id):
        # Установка сессии и проверка наличия
        db_item = self.db.session.query(SQLBook).get(id)
        if db_item:
            db.session.delete(db_item)
            db.session.commit()
            return (
                {
                    "ResponseText": "Item successfully deleted"
                }
            )
        return (
            {
                "ResponseText": "Bad Request. Such ID doesn't exists"
            }
        )

    def update(self, new_item, id):
        # Создаем запрос к таблице Book и фильтруем записи по ID
        query = db.session.query(SQLBook).filter(SQLBook.id == id).first()
        # Если существует, то дальнейший код, если нет, то 401
        existing_item = db.session.query(SQLBook).filter(SQLBook.id == id).first()
    
        if existing_item:
            # Обновляем атрибуты записи
            existing_item.title = new_item.title
            existing_item.publish_year = new_item.publish_year
            existing_item.pages_count = new_item.pages_count
            existing_item.description = new_item.description
            existing_item.created_at = datetime.strptime(new_item.created_at, "%Y-%m-%d")
            db.session.commit()
            return {
                "Response": 200,
                "ResponseText": "Item successfully updated"}
        return {
            "Response": 401,
            "ResponseText": "Bad Request. Such ID doesn't exists"
        }

    def get(self):
        items = self.db.session.query(SQLBook).all()
        return [item for item in items]

    def get_by_id(self, id: int):
        item = self.db.session.query(SQLBook).get(id)
        if item:
            return item
        return {
            "Response": 401,
            "ResponseText": "Bad Request. Such ID doesn't exists"
        }
