import os

import json
from http import HTTPStatus
from pprint import pprint

import requests


_BOOKS_FIXTURE = "books_fixture.json"

BOOKS_SERVICE_URL = "http://localhost:5001/books"

_CLIENTS_FIXTURE = "clients_fixture.json"

CLIENTS_SERVICE_URL = "http://localhost:5002/clients"

_RENTALS_FIXTURE = "rentals_fixture.json"

RENTALS_SERVICE_URL = "http://localhost:5003/rentals"

_script_dir = os.path.dirname(__file__)


def _load_fixture(loc):
    path = os.path.join(_script_dir, loc)

    with open(path, "r") as file:
        dados = json.load(file)

    return dados



def _post_initial_books(books):
    books_created = []
    for book in books:
        response = requests.post(BOOKS_SERVICE_URL, json=book)
        if response.status_code == HTTPStatus.CREATED:
            created_book = response.json()
            books_created.append(created_book)
            print("Livro", created_book["id"], created_book["author"], "criado com sucesso!")
    
    return len(books_created), tuple(_book["id"] for _book in books_created) 



def _post_initial_clients(clients):
    clients_created = []
    for client in clients:
        response = requests.post(CLIENTS_SERVICE_URL, json=client)
        if response.status_code == HTTPStatus.CREATED:
            created_client = response.json()
            clients_created.append(created_client)
            print("Cliente", created_client["id"], created_client["cpf"], "criado com sucesso!")

    return len(clients_created), tuple(_client["id"] for _client in clients_created)



def _post_initial_rentals(rentals):
    rentals_created = []
    for rental in rentals:
        response = requests.post(RENTALS_SERVICE_URL, json=rental)
        if response.status_code == HTTPStatus.CREATED:
            created_rental = response.json()
            rentals_created.append(created_rental)
            print("Empréstimo", created_rental["id"], "criado com sucesso!")

    return len(rentals_created), tuple(_rental["id"] for _rental in rentals_created)



def main():
    print('Iniciando migração com população inicial do serviço')

    for fixture in (_BOOKS_FIXTURE, _CLIENTS_FIXTURE, _RENTALS_FIXTURE): 
        dados = _load_fixture(fixture)
        if fixture == _BOOKS_FIXTURE:
            count, ids = _post_initial_books(dados["books"])
            print(count, "livros criados com sucesso")
            pprint(ids)
        elif fixture == _CLIENTS_FIXTURE:
            count, ids = _post_initial_clients(dados["clients"])
            print(count, "clientes criados com sucesso")
            pprint(ids)
        elif fixture == _RENTALS_FIXTURE:
            count, ids = _post_initial_rentals(dados["rentals"])
            print(count, "aluguéis criados com sucesso")
            pprint(ids)

    print("População de dados inicial do serviço realizada com sucesso")


if __name__ == "__main__":
    main()
