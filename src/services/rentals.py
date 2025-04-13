from http import HTTPStatus

from flask import Flask, request

from database.managers import list_clients, create_new_client

app = Flask(__name__)

API_INFO = {
    "version": "0.0.1",
    "description": "Aplicação REST* que cuida do domínio de empréstimo (`clients`) para serviço composto de biblioteca"
}

ALIVE = "ALIVE"


@app.get("/")
def api_root():
    return API_INFO, HTTPStatus.OK



@app.get("/alive")
def alive_smoke_test():
    return {"status": ALIVE}, HTTPStatus.OK



@app.get('/rentals')
def clients_list():
    clients = list_clients()

    return {
        "clients": clients,
        "count": len(clients)
    }, HTTPStatus.OK



@app.post("/rentals")
def clients_create():
    try:
        request_data = request.get_json()
        name = request_data["name"]
        cpf = request_data["cpf"]
        birth_date = request_data["birth_date"]
        email = request_data["email"]
        address = request_data["address"]
    except KeyError:
        return "JSON body params `name`, `cpf`, `birth_date`, `email` and `address` are mandatory", HTTPStatus.BAD_REQUEST

    new_book = create_new_client(name, cpf, birth_date, email, address)

    return new_book, HTTPStatus.CREATED
