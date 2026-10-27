API Filmes
API de gerenciamento de filmes desenvolvida com FastAPI, SQLAlchemy e SQLite.

Funcionalidades
Adicionar filmes
Listar todos os filmes
Buscar filme por ID
Buscar filmes por gênero
Atualizar filmes existentes
Excluir filmes
Tecnologias Utilizadas
Python
FastAPI
SQLAlchemy
SQLite
Estrutura do Projeto
api_filmes/
│
├── main.py
├── database.py
├── models.py
├── filmes_routers.py
└── README.md
Instalação
Clone o repositório:

git clone https://github.com/Vitor-Eduardo-Bastos/api_filmes.git
Acesse a pasta do projeto:

cd api_filmes
Instale as dependências:

pip install fastapi uvicorn sqlalchemy
Executando a Aplicação
python -m uvicorn main:app --reload
A API ficará disponível em:

http://127.0.0.1:8000
Documentação Interativa
Após iniciar a aplicação, acesse:

http://127.0.0.1:8000/docs
Objetivo do Projeto
Este projeto foi desenvolvido para praticar conceitos de desenvolvimento backend com Python, incluindo:

Criação de APIs REST
Operações CRUD
Organização de rotas com APIRouter
Integração com banco de dados SQLite
Utilização do SQLAlchemy como ORM
