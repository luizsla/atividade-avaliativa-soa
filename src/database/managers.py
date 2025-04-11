import psycopg

from uuid import uuid4

from .queries import CREATE_BOOK_QUERY, LIST_BOOKS_QUERY


def list_books():
    with psycopg.connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(LIST_BOOKS_QUERY)
            books_rows = cursor.fetchall()

    return [{} for row in books_rows]


def create_new_book(title, author, keywords, isbn_10):
    with psycopg.connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(CREATE_BOOK_QUERY, (str(uuid4()), title, author, keywords, isbn_10))

        return cursor.rowcount == 1