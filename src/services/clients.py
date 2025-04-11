from http import HTTPStatus

from flask import Flask, request

from database.managers import list_books, create_new_book

app = Flask(__name__)