FROM python:3-slim

RUN pip install poetry==1.0.0b3

WORKDIR /code
COPY pyproject.toml /code/

RUN poetry config virtualenvs.create false && \
    poetry install $(test "$ENV" = production && echo "--no-dev") --no-interaction --no-ansi

COPY sistema_portuario/ /code/sistema_portuario/

WORKDIR /code/sistema_portuario

CMD PYTHONPATH=.. python manage.py runserver --noreload 0.0.0.0:$PORT
