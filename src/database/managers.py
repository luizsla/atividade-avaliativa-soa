import psycopg
from psycopg.types.json import Json

from uuid import uuid4

from decouple import config

from .queries import (
    CREATE_BOOK_QUERY,
    CREATE_CLIENT_QUERY,
    CREATE_RENTAL_QUERY,
    GET_BOOK_BY_ID_QUERY,
    GET_CLIENT_BY_ID_QUERY,
    GET_RENTAL_BY_ID_QUERY,
    LIST_BOOKS_QUERY,
    LIST_CLIENTS_QUERY,
    LIST_RENTALS_QUERY
)


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



def __transform_clients_tuple_to_dict(row):
    return {
        "id": row[0],
        "name": row[1],
        "cpf": row[2],
        "birth_date": row[3],
        "email": row[4],
        "address": row[5]
    }



def list_clients():
    with psycopg.connect(CON_STRING) as conn:
        with conn.cursor() as cursor:
            cursor.execute(LIST_CLIENTS_QUERY)
            clients_row = cursor.fetchall()

    return [__transform_clients_tuple_to_dict(row) for row in clients_row]



def create_new_client(name, cpf, birth_date, email, address):
    primary_key = uuid4()
    birth_date_psql = "{year}-{month}-{day}".format(
        year=birth_date[-4:], month=birth_date[3:5], day=birth_date[:2]
    )

    with psycopg.connect(CON_STRING) as conn:
        with conn.cursor() as cursor:
            cursor.execute(CREATE_CLIENT_QUERY, (
                str(primary_key), name, cpf, birth_date_psql, email, Json(address)
            ))

            if cursor.rowcount == 1:
                cursor.execute(GET_CLIENT_BY_ID_QUERY, (primary_key,))
                newly_created_book = cursor.fetchone()
                return __transform_clients_tuple_to_dict(newly_created_book)



def __transform_rentals_tuple_to_dicr(row):
    return {
        "id": row[0],
        "client_id": row[1],
        "rented_books": row[2],
        "rental_date": row[3],
        "return_date": row[4]
    }



def list_rentals():
    with psycopg.connect(CON_STRING) as conn:
        with conn.cursor() as cursor:
            cursor.execute(LIST_RENTALS_QUERY)
            rentals_row = cursor.fetchall()

    return [__transform_rentals_tuple_to_dicr(row) for row in rentals_row]



def create_new_rental(client_id, rented_books, rental_date, return_date):
    primary_key = uuid4()
    rental_date_psql = "{year}-{month}-{day}".format(
        year=rental_date[-4:], month=rental_date[3:5], day=rental_date[:2]
    )
    return_date_psql = "{year}-{month}-{day}".format(
        year=return_date[-4:], month=return_date[3:5], day=return_date[:2]
    )

    with psycopg.connect(CON_STRING) as conn:
        with conn.cursor() as cursor:
            cursor.execute(CREATE_RENTAL_QUERY, (
                str(primary_key), client_id, rented_books, rental_date_psql, return_date_psql
            ))

            if cursor.rowcount == 1:
                cursor.execute(GET_RENTAL_BY_ID_QUERY, (primary_key,))
                newly_created_book = cursor.fetchone()
                return __transform_rentals_tuple_to_dicr(newly_created_book)
