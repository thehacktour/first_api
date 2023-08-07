

# API de Cadastro de Livros

Esta é uma API simples para cadastrar e visualizar informações básicas de livros.

## Funcionalidades

- Listar todos os livros
- Cadastrar um novo livro
- Visualizar detalhes de um livro específico




## Endpoints

#### Listar todos os livros

```http
  GET /api/books/
```

#### Visualizar detalhes de um livro específico

```http
  GET /api/books/{id}/
```

#### Cadastrar um novo livro

```http
  POST /api/books/

  Exemplo de corpo da solicitação:
{
    "title": "Livro Teste",
    "author": "Autor do Livro",
    "year": 2023,
    "genre": "Gênero do Livro"
}
```


## Instalação

Clone o repositório

```bash
  git clone https://github.com/seu-usuario/api-cadastro-livros.git
cd api-cadastro-livros

```
    
Instale as dependências:
```bash
  pip install -r requirements.txt

```

Execute a aplicação:
```bash
  python manage.py runserver

```
