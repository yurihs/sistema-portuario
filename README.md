
# Sistema Portuário

Projeto da disciplina de Engenharia de Software

Veja o sistema rodando: [https://sistema-portuario.herokuapp.com/](https://sistema-portuario.herokuapp.com/)

## Desenvolvimento

Estas são as etapas para executar o projeto:

1. Instalar o [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
2. ```docker build -t sistema-portuario .```
3. ```docker run -p 5000:5000 -e FLASK_ENV=development sistema-portuario```
4. Acessar http://localhost:5000/
