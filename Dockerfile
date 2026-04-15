FROM python:3

RUN apt update && apt install -y --no-install-recommends curl ca-certificates

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin/:$PATH"

WORKDIR /application

COPY . .

RUN uv sync
CMD ["uv", "run", "uvicorn", "src.app.main:app", "--host", "0.0.0.0"]
