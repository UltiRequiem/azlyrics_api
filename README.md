# [AZLyrics](https://www.azlyrics.com) API

[![CI](https://github.com/UltiRequiem/azlyrics_api/actions/workflows/ci.yaml/badge.svg)](https://github.com/UltiRequiem/azlyrics_api/actions/workflows/ci.yaml)

An API interface for azlyrics, it uses [azapi](https://github.com/elmoiv/azapi)
under the hood.

<div align="center">
  <img src="./assets/cover.png" />
</div>

## Docs

Check the
[automatic generated docs by Swagger](https://azlyrics.herokuapp.com/docs).

## Development

1. Install [Poetry](https://python-poetry.org)

2. Install dependencies and enter to virtual environment

```sh
poetry shell && poetry install
```

3. Put `ENV=development` in your `.env` file

4. Start the process

```sh
python run.py
```

## Production

1. Install [Docker](https://docs.docker.com/get-docker)

2. Build the image

```sh
docker build . -t ultirequiem/azlyrics_api
```

3. Run the image

```sh
docker run -p 8080:8080 -d ultirequiem/azlyrics
```

## Licence

This project is licensed under the MIT Licence.
