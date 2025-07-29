
.PHONY : help
help:  ## Use one of the following instructions:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY : lint
lint : ## Static code analysis with Pylint
	pylint -ry climada > pylint.log || true

.PHONY : test
test : ## Run tests
	@uv run pytest -x \
		-n auto \
		--cov src \
		--cov-report term-missing

