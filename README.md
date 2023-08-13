

# API de Cadastro de Livros 📚

Esta é uma API simples para cadastrar e visualizar informações básicas de livros.

## Funcionalidades 📋

- Listar todos os livros
- Cadastrar um novo livro
- Visualizar detalhes de um livro específico




## Endpoints 

#### Listar todos os livros

```http
  GET https://listbooks-api.onrender.com/books/
```

#### Visualizar detalhes de um livro específico

```http
  GET https://listbooks-api.onrender.com/books/{id}/
```

#### Cadastrar um novo livro

```http
  POST https://listbooks-api.onrender.com/books/

  Exemplo de corpo da solicitação:
{
    "title": "Livro Teste",
    "author": "Autor do Livro",
    "year": 2023,
    "genre": "Gênero do Livro"
}
```


## Instalação 🚀

1. Clone o repositório

```bash
  git clone https://github.com/luluoliv/first_api.git
  cd first_api

```
    
2. Instale as dependências:
```bash
  pip install poetry
  poetry install
  poetry shell

```

3. Execute a aplicação:
```bash
  python manage.py runserver

```
4. Use o endpoint:

``` bash
  http://localhost:8000/api/books
```

## Contribuição 🤝
Contribuições são bem-vindas! Se você encontrar algum problema ou tiver uma ideia de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença 📜
Este projeto está licenciado sob a MIT License.
