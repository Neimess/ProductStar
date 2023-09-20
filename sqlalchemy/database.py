from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement= True)
    name = db.Column(db.String)
    author = db.Column(db.String, nullable = True)
    is_read = db.Column(db.Boolean)
    genre_name = db.Column(db.String, db.ForeignKey("genre.name", ondelete='SET NULL'))
    genre = relationship("Genre", back_populates="books")

class Genre(db.Model):
    name = db.Column(db.String, primary_key = True)
    books = relationship(
        "Book", back_populates="genre"
    )