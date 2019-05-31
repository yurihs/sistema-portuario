FROM node:12 AS node_build

COPY package.json .
COPY package-lock.json .
COPY build.js .

RUN npm install && npm run build

FROM python:3-slim

COPY app app
COPY config.py .
COPY requirements.txt .
COPY --from=node_build dist app/assets/vendor
RUN pip install -r requirements.txt

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]

EXPOSE 5000
