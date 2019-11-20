# Sistema Portuário

Projeto da disciplina de Engenharia de Software

Veja o sistema rodando:

* [https://sistema-portuario-backend.herokuapp.com/](https://sistema-portuario-backend.herokuapp.com/) (Apenas o backend)

## Desenvolvimento

Estas são as etapas para executar o projeto:

### Com o Docker

Pré-requisitos:
* [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [Docker Compose](https://docs.docker.com/compose/install/)

1. Criar um arquivo de configurações. Use o de exemplo como base: ```cp backend/.env.sample backend/.env```
2. ```docker-compose up -d```
3. Acessar a documentação da API em http://localhost:8000/api/swagger/  
   Usuário padrão: admin@example.com, 123

### Manualmente

Pré-requisitos:
* Python 3

#### Backend

1. Entrar no diretório da aplicação de backend
   ```sh
   cd backend/sistema_portuario/
   ```
2. Instalar o gerenciador de pacotes [Poetry](https://poetry.eustace.io/):
   ```sh
   pip install --user --pre poetry
   ```
3. Adicionar o caminho de instalação local do pip à variável de ambiente PATH
   ```sh
   export PATH="$PATH:$HOME/.local/bin"
   ```
4. Usar o Poetry para instalar as dependências Python do projeto:
   ```sh
   poetry install
   ```
5. Criar um arquivo de configurações. Use o de exemplo como base:
   ```sh
   cp ../.env.sample ../.env
   ```
6. Inicializar o banco de dados
   ```sh
   poetry run python manage.py migrate
   ```
7. Carregar dados iniciais do banco (obrigatório)
   ```sh
   poetry run python manage.py loaddata essencial
8. Gerar dados de exemplo (opcional)
   ```sh
   poetry run python manage.py popular_com_exemplos
   ```
9. Executar a aplicação
   ```sh
   poetry run python manage.py runserver
   ```
10. Acessar a documentação da API em http://localhost:8000/api/swagger/  
   Usuário padrão: admin@example.com, 123


## Testes

Rodar os testes do backend:

```
cd backend
PYTHONPATH=sistema_portuario poetry run pytest
```
