from flask import Flask

app = Flask(__name__)


@app.get('/books')
def books_list():
    return {
        "books": [
            {
                "id": 1,
                "title": "1984",
                "author": "George Orwell",
                "keywords": ["ficção científica", "ficção política"],
                "isbn-10": "8535932968"
            },
            {
                "id": 2,
                "title": "A mulher ruiva",
                "author": "Author B",
                "keywords": ["ficção literária"],
                "isbn-10": "8535934073"
            },
            {
                "id": 3,
                "title": "Os sofrimentos do jovem Werther",
                "author": "Johann Wolfgang von Goethe",
                "keywords": ["romance epistolar", "ficção autobiográfica"],
                "isbn-10": "658649012X"
            },
            {
                "id": 4,
                "title": "Don Casmurro",
                "author": "Machado de Assis",
                "keywords": ["literatura brasileira", "romance", "realismo literário"],
                "isbn-10": "8508040814"
            },
            {
                "id": 5,
                "title": "Só garotos",
                "author": "Patti Smith",
                "keywords": ["biografia", "música", "arte"],
                "isbn-10": "8535930590"
            }
        ]
    }



@app.post("/books")
def books_create():
    pass



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True,)