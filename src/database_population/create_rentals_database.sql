CREATE DATABASE bookstore;

\c bookstore;

CREATE TABLE rentals (
    id UUID PRIMARY KEY,
    client_id UUID NOT NULL,
    rented_books UUID[],
    rental_date DATE NOT NULL,
    return_date DATE NOT NULL
);