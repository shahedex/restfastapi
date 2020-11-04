# fastapi-rest
High-performance Async REST API, in Python. FastAPI + Uvicorn.

# Run locally using Poetry
## 1. Install Poetry
```bash
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
$ poetry --version
```

## 2. Install dependencies
```bash
$ poetry shell
$ poetry install
```

## 3. Run with Poetry with hot-reload
```bash
$ poetry run task app
```
**or**
## 3. Run with default Python with debug info
```bash
$ python app/main.py
```
# Run with docker
```bash
$ docker build -t fastapi-rest .
$ docker run -p 80:80 fastapi-rest
```