import time
import sys
import os

from pprint import pprint
from http import HTTPStatus

import requests


BOOKS_SERVICE_URL = "http://localhost:5000"

CLIENTS_SERVICE_URL = "http://localhost:5001"


def _smoke_test_books_service():
    response = requests.get(BOOKS_SERVICE_URL + "/alive")
    if response.status_code == HTTPStatus.OK:
        return response.json()["status"] == "ALIVE"

    return False



def _smoke_test_clients_service():
    response = requests.get(CLIENTS_SERVICE_URL + "/alive")
    if response.status_code == HTTPStatus.OK:
        return response.json()["status"] == "ALIVE"

    return False



def _fetch_books():
    print("Consultando servioço de livros em", BOOKS_SERVICE_URL)

    response = requests.get(BOOKS_SERVICE_URL + "/books")
    if response.status_code == HTTPStatus.OK:
        json_response = response.json()
        return json_response["books"], json_response["count"]

    print("Livros recuperados com sucesso!")
    
    return [], 0



def _fetch_clients():
    print("Consultando serviço de clientes em", CLIENTS_SERVICE_URL)

    response = requests.get(CLIENTS_SERVICE_URL + "/clients")
    if response.status_code == HTTPStatus.OK:
        json_response = response.json()
        return json_response["clients"], json_response["count"]

    print("Clientes recuperados com sucesso!")

    return [], 0



def main():
    while True:
        if _smoke_test_books_service():
            books, count = _fetch_books()
            print("Existem", count, "Livros na API de livros")
            pprint(books)
        else:
            print("Serviço de livros está fora do ar, tentando conectar novamente em segundos...")

        if _smoke_test_clients_service():
            clients, count = _fetch_clients()
            print("Existem", count, "Clientes na API de clientes")
            pprint(clients)
        else:
            print("Serviço de clientes está fora do ar, tentando conectar novamente em segundos...")

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