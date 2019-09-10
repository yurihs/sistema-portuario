
# Sistema Portuário

Projeto da disciplina de Engenharia de Software

Veja o sistema rodando: [https://sistema-portuario.herokuapp.com/](https://sistema-portuario.herokuapp.com/)

## Desenvolvimento

Estas são as etapas para executar o projeto:

### Com o Docker

Pré-requisito: [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

1. ```docker build -t sistema-portuario .```
2. ```docker run -p 5000:5000 -e PORT=5000 -e FLASK_ENV=development sistema-portuario```
3. Acessar http://localhost:5000/

### Manualmente

Pré-requisitos:
- Python 3 e virtualenv
- Node.js e NPM

1. Criar e ativar um virtualenv com o Python 3:
   ```
   python3 -m venv venv_sistema
   source venv_sistema/bin/activate
   ```
2. Instalar o gerenciador de pacotes [Poetry](https://poetry.eustace.io/):
   ```
   pip install poetry
   ```
3. Usar o Poetry para instalar as dependências Python do projeto:
   ```
   poetry install
   ```
4. Usar o NPM para instalar as dependências JS e CSS do projeto:
   ```
   npm install
   ```
5. Extrair e mover as dependências instaladas pelo NPM para dentro da aplicação:
    ```
    npm run build
    rm -rf app/assets/vendor
    mv dist/static/* app/static
    mv dist app/assets/vendor
    ```
6. Inicializar o banco de dados
   ```
   FLASK_ENV=development python manage.py initdb
   ```
7. Executar o aplicativo Flask em modo de desenvolvimento:
   ```
   FLASK_ENV=development flask run
   ```
8. Acessar http://localhost:5000/
