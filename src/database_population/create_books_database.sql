-- Aqui criaremos o banco books
CREATE DATABASE BOOKSTORE;

CREATE TABLE books (
    id UUID PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    keywords TEXT[],
    isbn_10 VARCHAR(20) UNIQUE
);