

# API de Cadastro de Livros 📚

Esta é uma API simples para cadastrar e visualizar informações básicas de livros.

## Funcionalidades 📋

- Listar todos os livros
- Cadastrar um novo livro
- Visualizar detalhes de um livro específico




## Endpoints 

#### Listar todos os livros

```http
  GET /{localhost}/books/
```

#### Visualizar detalhes de um livro específico

```http
  GET /{localhost}/books/{id}/
```

#### Cadastrar um novo livro

```http
  POST /{localhost}/books/

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
  git clone https://github.com/seu-usuario/api-cadastro-livros.git
  cd api-cadastro-livros

```
    
2. Instale as dependências:
```bash
  pip install -r requirements.txt

```

3. Execute a aplicação:
```bash
  python manage.py runserver

```

## Contribuição 🤝
Contribuições são bem-vindas! Se você encontrar algum problema ou tiver uma ideia de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença 📜
Este projeto está licenciado sob a MIT License.
