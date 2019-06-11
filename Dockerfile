FROM node:12 AS node_build

COPY package.json package-lock.json build.js ./

RUN npm install && npm run build

FROM python:3-slim

RUN pip install poetry==0.12.16

WORKDIR /code
COPY pyproject.toml /code/

RUN poetry config settings.virtualenvs.create false && \
    poetry install $(test "$FLASK_ENV" = production && echo "--no-dev") --no-interaction --no-ansi

COPY . /code
COPY --from=node_build dist /code/app/assets/vendor
COPY --from=node_build dist/static /code/app/static/

CMD flask run -h 0.0.0.0 -p $PORT
