.PHONY: test lint format typing clean

run:
	docker compose up --build
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
	rm -rf ./alembic/__pycache__/
	rm -rf ./app/__pycache__/
	rm -rf ./app/api/__pycache__/
	docker compose down -v
