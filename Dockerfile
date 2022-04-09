FROM python:3.10.4

WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry==1.1.11 && poetry install

COPY . .

EXPOSE 8080

CMD ["python", "run.py" ]
