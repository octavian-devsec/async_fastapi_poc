.PHONY: test lint format typing clean

run:
	docker compose up --build
new_migration:
	docker exec -it async_fastapi_poc-api-1 uv run python -m alembic revision --autogenerate
	sudo chown ${USER}:${USER} ./src/migrations/versions/*
test:
	docker exec -it async_fastapi_poc-api-1 uv run python -m pytest -s
lint:
	uv run ruff check .
format:
	uv run ruff format --diff .
typing:
	uv run mypy .
clean:
	rm -rf ./__pycache__/
	rm -rf ./.mypy_cache/
	rm -rf ./.pytest_cache/
	rm -rf ./.ruff_cache/
	rm -rf ./tests/__pycache__/
	rm -rf ./migrations/__pycache__/
	rm -rf ./migrations/versions/__pycache__/
	rm -rf ./app/__pycache__/
	rm -rf ./app/api/__pycache__/
