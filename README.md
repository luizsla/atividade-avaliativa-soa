# Library

Sistema de demonstração de funcionalidades de uma aplicação orientada a serviços distribuída. Esse projeto foi desenvolvido como atividade avaliativa da disciplina de *Desenvolvimento de Aplicações Orietada a Serviços* ministrada pelo professor Luis Paulo Carvalho.

## Requisitos da aplicação

- Docker + docker-compose
- python3 (versão utilizada 3.11)
- Portas `5001`, `5002` e `5003` livres

## Composição da aplicação

Essa aplicação é composta de _três_ serviços que represental domínios de uma aplicação de biblioteca, os serviços gerenciam acervo (serviço `books`), tomador-empréstimo (serviço `clients`) e empréstimos (serviço `rentals`).

Os serviços são acessíveis via interfaces REST (foram criados em cada API os endpoits *C*reate and *R*ead) e se encontram *containerizados* para possível deploy como aplicações auto-contidas. São componentes úteis da aplicação:

- Serviço `books` disponível na porta 5001
- Serviço `clients` disponível na porta 5002
- Servço `rentals` disponível na porta 5003
- Script de população inicial de dados (disponível em `/src/database_population/database_population.py`)
- Cliente tipo crowler para chamada dos serviços (disponível em `src/clients/crowler.py`)

### Serviço de gerenciamento de acervo (`books`)

Rotas disponíveis em:

- `http://localhost:5001/`
- [GET, POST] `http://localhost:5001/books`

Exemplo de *payload* para cadastro de livro:
```
{
    "id": "c902a156-1c37-47b3-8e6b-408ed4e5fbc6",
    "title": "1984",
    "author": "George Orwell",
    "keywords": ["ficção científica", "ficção política"],
    "isbn-10": "8535932968"
}
```

### Serviço de gerenciamento de tomadores-empréstimo (`clients`)

Rotas disponíveis em:

- `http://localhost:5002/`
- [GET, POST] `http://localhost:5001/clients`

Exemplo de *payload* para cadastro de cliente:
```
{
    "id": "243f6c52-279d-4b21-813b-791d619702ad",
    "name": "Carlos Eduardo Anthony Silveira",
    "cpf": "109.059.705-35",
    "birth_date": "04/03/2002",
    "email": "carlos_silveira@inglesasset.com.br",
    "address": {
        "cep": "44180-970",
        "street": "Praça da Matriz 163 - Centro",
        "city": "Antônio Cardoso",
        "number": "217",
        "state": "BA"
    }
}
```

### Serviço de gerenciamento de empréstimos (`rentals`)

Rotas disponíveis em:

- `http://localhost:5003/`
- [GET, POST] `http://localhost:5001/rentals`

Exemplo de *payload* para cadastro de empréstimo:
```
{
    "id": "7063e6ff-6d34-48ac-9bdd-9174c9b30ee8",
    "client_id": "de3f0678-36c5-4f21-a017-fb4f554c3d74",
    "rented_books": [
        "b1297024-ab29-45ca-8d17-d1ed02d6cd00",
        "bb1ad814-2a99-4d24-8d15-ba2e84ba648a",
        "c902a156-1c37-47b3-8e6b-408ed4e5fbc6"
    ],
    "rental_date": "02/03/2025",
    "return_date": "17/03/2025"
}
```

## Instalação e execução dos serviços

1- Baixe a aplicação no diretório desejado

2- Dentro do diretório digite `docker compose up` para subir os containers da aplicação

3 - Quando finalizado digite `docker compose down` para limpar a arquitetura Docker

4 - Os scripts de `database_population.py` e `crowler.py` podem ser executados de dentro do continer ou no host local.

4.1 - Para execução dos scripts em host local criar um ambiente virtual com `python3 -m venv .venv`

4.2 - Entrar no ambinete virtual criado com `source .venv/bin/activate`

4.3 - Instalar as dependências do ambinete com `pip3 install -r requirements.txt`

