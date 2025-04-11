import psycopg

from uuid import uuid4

from decouple import config

from .queries import CREATE_BOOK_QUERY, GET_BOOK_BY_ID_QUERY, LIST_BOOKS_QUERY


CON_STRING = config("DATABASE_CONNECTION_STRING")


def __transform_books_tuple_to_dict(row):
    return {
        "id": row[0],
        "title": row[1],
        "author": row[2],
        "keywords": row[3],
        "isbn_10": row[4]
    }


def list_books():
    with psycopg.connect(CON_STRING) as conn:
        with conn.cursor() as cursor:
            cursor.execute(LIST_BOOKS_QUERY)
            books_rows = cursor.fetchall()

    return [__transform_books_tuple_to_dict(row) for row in books_rows]



def create_new_book(title, author, keywords, isbn_10):
    primary_key = uuid4()

    with psycopg.connect(CON_STRING) as conn:
        with conn.cursor() as cursor:
            cursor.execute(CREATE_BOOK_QUERY, (str(primary_key), title, author, keywords, isbn_10))

            if cursor.rowcount == 1:
                cursor.execute(GET_BOOK_BY_ID_QUERY, (primary_key,))
                newly_created_book = cursor.fetchone()
                return __transform_books_tuple_to_dict(newly_created_book)