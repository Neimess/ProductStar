from flask import Flask
from context import Context
from views.book import bp as book_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(book_bp, url_prefix="/books")
    #Контекст передается для работы с db.init_app(app)
    with app.app_context():
        app.config["CONTEXT"] = Context(app)

    return app


app = create_app()
