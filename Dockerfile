FROM python:3.13.12-alpine

WORKDIR /application

COPY ./application /application/application
COPY pyproject.toml /application
COPY uv.lock /application

RUN pip install uv
RUN uv sync

EXPOSE 80

CMD ["uv", "run", "uvicorn", "application.run:create_app", "--host", "0.0.0.0", "--port", "80"]
