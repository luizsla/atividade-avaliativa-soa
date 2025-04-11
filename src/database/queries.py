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

LIST_BOOKS_QUERY = """
    SELECT * FROM books;
"""