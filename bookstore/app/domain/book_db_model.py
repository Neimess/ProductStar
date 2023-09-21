from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class SQLBook(db.Model):
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String)
    publish_year = db.Column(db.Integer)
    pages_count = db.Column(db.Integer)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime)
