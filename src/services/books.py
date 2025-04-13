from http import HTTPStatus

from flask import Flask, request

from database.managers import list_books, create_new_book

app = Flask(__name__)


@app.get('/books')
def books_list():
    books = list_books()

    return {
        "books": books,
        "count": len(books)
    }, HTTPStatus.OK



@app.post("/books")
def books_create():
    try:
        request_data = request.get_json()
        title = request_data["title"]
        author = request_data["author"]
        keywords = request_data["keywords"]
        isbn_10 = request_data["isbn_10"]
    except KeyError:
        return "JSON body params `title`, `author`, `keywords` and `isbn_10` are mandatory", HTTPStatus.BAD_REQUEST

    new_book = create_new_book(title, author, keywords, isbn_10)

    return new_book, HTTPStatus.CREATED
