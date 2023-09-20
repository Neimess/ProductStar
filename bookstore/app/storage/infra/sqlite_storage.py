from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .mem_storage import MemoryStorage
from domain.book_db_model import SQLBook, db
from domain.book import Book


class SQLiteStorage(MemoryStorage):
    def __init__(self, app=None, database_uri="sqlite:///test.db"):
        self.database_uri = database_uri
        self.db = db
        self.engine = create_engine(self.database_uri)
        if app is not None:
            self.__init_app__(app)

    def __init_app__(self, app):
        self.app = app
        self.app.config["SQLALCHEMY_DATABASE_URI"] = self.database_uri
        self.db.init_app(app)

    def add(self, item: Book):
        with self.app.app_context():
            db.create_all()
            Session = sessionmaker(bind=self.engine)
            session = Session()
            print("db_created")
            db_item = SQLBook(
                title=item.title,
                publish_year=item.publish_year,
                pages_count=item.pages_count,
                description=item.description,
                created_at=item.created_at)
            session.add(db_item)
            session.commit()
            return db_item.id

    # def delete(self, item_id):
    #     with self.app.app_context():
    #         session = sessionmaker(bind=self.db.engine)()
    #         db_item = session.query(Book).get(item_id)
    #         if db_item:
    #             session.delete(db_item)
    #             session.commit()
    #         session.close()

    # def update(self, item_id):
    #     with self

    # def get(self):
    #     with self.app.app_context():
    #         session = sessionmaker(bind=self.db.engine)()
    #         items = session.query(Book).all()
    #         session.close()
    #         return [item for item in items]
