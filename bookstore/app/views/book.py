from flask import Blueprint, current_app, request, jsonify, json
from flask.json import JSONEncoder

from context import get_context
from domain.book import Book
from encoders.json_encoder import CustomJSONEncoder

bp = Blueprint("book", __name__)
bp.json_encoder = CustomJSONEncoder


@bp.route("/")
def get_books():
    ctx = get_context(current_app)
    return jsonify(ctx.book_service.get(), 200)


@bp.route("/<int:id>", methods=["GET"])
def get_book_by_id(id):
    ctx = get_context(current_app)
    return jsonify(ctx.book_service.get_by_id(id))


@bp.route("/", methods=["POST"])
def add_book():
    ctx = get_context(current_app)
    book = Book(**request.json)
    book_id = ctx.book_service.add(book)
    if book_id is not None:
        return jsonify({"id": book_id, "book": book}, 200)
    return jsonify({"Something went wrong"}, 400)


@bp.route("/<int:id>", methods=["DELETE"])
def delete_book(id):
    ctx = get_context(current_app)
    response = ctx.book_service.delete(id)
    if response:
        return jsonify(response, 200)

@bp.route("<int:id>", methods=["PATCH"])
def update_book(id):
    ctx = get_context(current_app)
    book = Book(**request.json)
    response = ctx.book_service.update(book, id)
    return jsonify(response)