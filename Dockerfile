FROM python:3.9.7

WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry 

RUN poetry install

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", " azlyrics:app", "--host=0.0.0.0", "--port=8000" ]
