from http import HTTPStatus

from flask import Flask, request

from database.managers import list_rentals, create_new_rental

app = Flask(__name__)

API_INFO = {
    "version": "0.0.1",
    "description": "Aplicação REST* que cuida do domínio de empréstimo (`rentals`) para serviço composto de biblioteca"
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
    rentals = list_rentals()

    return {
        "rentals": rentals,
        "count": len(rentals)
    }, HTTPStatus.OK



@app.post("/rentals")
def clients_create():
    try:
        request_data = request.get_json()
        client_id = request_data["client_id"]
        rented_books = request_data["rented_books"]
        rental_date = request_data["rental_date"]
        return_date = request_data["return_date"]
    except KeyError:
        return "JSON body params `client_id`, `rented_books`, `rental_date` and `return_date` are mandatory", HTTPStatus.BAD_REQUEST

    new_book = create_new_rental(client_id, rented_books, rental_date, return_date)

    return new_book, HTTPStatus.CREATED
