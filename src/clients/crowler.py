import time
import sys
import os

from pprint import pprint
from http import HTTPStatus

import requests


BOOKS_SERVICE_URL = "http://localhost:5000/books"

CLIENTS_SERVICE_URL = "http://localhost:5001/clients"


def _fetch_books():
    print("Consultando servioço de livros em", BOOKS_SERVICE_URL)

    response = requests.get(BOOKS_SERVICE_URL)
    if response.status_code == HTTPStatus.OK:
        json_response = response.json()
        return json_response["books"], json_response["count"]

    print("Livros recuperados com sucesso!")
    
    return [], 0



def _fetch_clients():
    print("Consultando serviço de clientes em", CLIENTS_SERVICE_URL)

    response = requests.get(CLIENTS_SERVICE_URL)
    if response.status_code == HTTPStatus.OK:
        json_response = response.json()
        return json_response["clients"], json_response["count"]

    print("Clientes recuperados com sucesso!")

    return [], 0



def main():
    while True:
        books, count = _fetch_books()
        print("Existem", count, "Livros na API de livros")
        pprint(books)

        clients, count = _fetch_clients()
        print("Existem", count, "Clientes na API de clientes")
        pprint(clients)

        time.sleep(5)



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Crowler interrompido graciosamente...')
        try:
            sys.exit(1)
        except SystemExit:
            os._exit(1)