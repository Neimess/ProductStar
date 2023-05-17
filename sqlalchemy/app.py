from flask import Flask, request, jsonify, abort
from flask import render_template
from database import db, Book, Genre
import os

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

    # fill DB with testing data(fixtures)
    detective = Genre(name="Детектив")
    db.session.add(detective)
    romane = Genre(name="Роман")
    db.session.add(romane)
    comedy = Genre(name="Комедия")
    db.session.add(comedy)

    holmes = Book(name = 'Шерлок Холмс', author= 'А.К. Дойл', genre=detective)
    db.session.add(holmes)
    onegin = Book(name="Евгений Онегин", author= 'А.С Пушкин', genre=romane)
    db.session.add(onegin)
    dubrovsky = Book(name="Дубровский", author= 'А.С Пушкин', genre=romane)
    db.session.add(dubrovsky)
    captain_daughter = Book(name="Капитанская дочка", author='А.С Пушкин', genre=romane)
    db.session.add(captain_daughter)
    gore_ot_uma = Book(name="Горе от ума", author='А.С Грибоедов', genre=comedy)
    db.session.add(gore_ot_uma)

    db.session.commit()
@app.route("/", methods=["GET", "POST"])
def all_books():
    books = Book.query.order_by(Book.id.desc()).limit(15).all()
    #books = Book.query.all()
    return render_template("all_books.html", books=books)

@app.route("/books/<book_id>", methods=['POST'])
def set_book_is_read(book_id):
    arg = request.form.get('is_read')

    dbsession = db.session
    query = dbsession.query(Book)
    record = query.filter(Book.id == book_id).first()
    # Если запись в таблице `Book` с переданным `book_id` не найдена, то возвращаем ошибку 404 "Not Found"
    if record is None:
        abort(404)

    if arg == 'on':
        record.is_read = True
    else:
        record.is_read = False

    dbsession.commit()

    # Возвращаем сообщение в зависимости от значения поля `is_read`
    if record.is_read:
        return f"Книга '{record.name}' отмечена как прочитанная"
    else:
        return f"Книга '{record.name}' отмечена как непрочитанная"

@app.route("/genre/<genre_name>")
def books_by_genre(genre_name):
    genre = Genre.query.get_or_404(genre_name)
    return render_template(
        "books_by_genre.html",
        genre_name=genre.name,
        books=genre.books,
    )

if __name__ == '__main__':
    app.run()