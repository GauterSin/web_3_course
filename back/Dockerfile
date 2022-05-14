FROM python:3.10


WORKDIR /code


COPY ./pyproject.toml /code/pyproject.toml


RUN pip install poetry

# RUN python3.10 -m venv venv && source venv/bin/activate
RUN poetry install --no-dev

COPY . /code
