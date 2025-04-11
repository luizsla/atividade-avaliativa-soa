CREATE DATABASE bookstore;

\c bookstore;

CREATE TABLE clients (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    birth_date DATE NOT NULL,
    email VARCHAR(255) unique not null,
    address json
);