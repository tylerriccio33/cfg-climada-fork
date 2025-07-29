
.PHONY : help
help:  ## Use one of the following instructions:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY : lint
lint : ## Run linters
	@uv run ruff format --exclude doc/
	@uv run ruff check --fix --exclude doc/
	@uv run ty check . --exclude doc/

.PHONY : test
test : ## Run tests
	@uv run pytest -x \
		-n auto \
		--cov src \
		--cov-report term-missing

