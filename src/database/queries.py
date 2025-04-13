from textwrap import dedent


CREATE_BOOK_QUERY = dedent("""
    INSERT INTO books (
        id,
        title,
        author,
        keywords,
        isbn_10
    ) VALUES (%s, %s, %s, %s, %s);
""")


GET_BOOK_BY_ID_QUERY = dedent("""
    SELECT * FROM books WHERE id = %s;
""")


LIST_BOOKS_QUERY = dedent("""
    SELECT * FROM books;
""")


CREATE_CLIENT_QUERY = dedent("""
    INSERT INTO clients (
        id,
        name,
        cpf,
        birth_date,
        email,
        address
    ) VALUES (%s, %s, %s, %s, %s, %s);
""")


GET_CLIENT_BY_ID_QUERY = dedent("""
    SELECT * FROM clients WHERE id = %s;
""")


LIST_CLIENTS_QUERY = dedent("""
    SELECT * FROM clients;
""")


CREATE_RENTAL_QUERY = dedent("""
    INSERT INTO rentals (
        id,
        client_id,
        rented_books,
        rental_date,
        return_date
    ) VALUES (
        %s, %s, %s, %s, %s
    );
""")


GET_RENTAL_BY_ID_QUERY = dedent("""
    SELECT * FROM rentals WHERE id = %s;
""")


LIST_RENTALS_QUERY = dedent("""
    SELECT * FROM rentals;
""")