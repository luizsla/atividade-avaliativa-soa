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
    SELECT * FROM books where id = %s
""")


LIST_BOOKS_QUERY = dedent("""
    SELECT * FROM books;
""")


