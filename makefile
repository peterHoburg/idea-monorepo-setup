lint:
	uv run ruff format
	uv run ruff check
	uv run ty check
	uv run pyright
	#uv run pyrefly check

test:
	uv run pytest -n auto
