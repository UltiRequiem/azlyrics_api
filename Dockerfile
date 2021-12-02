FROM python:3.9.9

WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry==1.1.11 && poetry install

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "python", "run.py"]
