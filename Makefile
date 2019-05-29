ifeq (${PYTHON}, )
override PYTHON=3.6
endif

DOCKER=docker run -p 8888:8888 -v ${PWD}:/ntc_rosetta ntc_rosetta-${PYTHON}:latest

.PHONY: build_test_container
build_test_container:
	docker build \
		--tag ntc_rosetta-${PYTHON}:latest \
		--build-arg PYTHON=${PYTHON} \
		-f Dockerfile .

.PHONY: build_test_containers
build_test_containers:
	make build_test_container PYTHON=3.6
	make build_test_container PYTHON=3.7

.PHONY: enter-container
enter-container:
	${DOCKER} \
		bash

.PHONY: pytest
pytest:
	${DOCKER} \
		pytest --cov=ntc_rosetta --cov-report=term-missing -vs ${ARGS}

.PHONY: black
black:
	${DOCKER} \
		black --check .

.PHONY: sphinx-test
sphinx-test:
	${DOCKER} \
		sphinx-build -W -n -E -q -N -b dummy -d docs/_build/doctrees docs /tmp/asd

.PHONY: pylama
pylama:
	${DOCKER} \
		pylama .

.PHONY: mypy
mypy:
	${DOCKER} \
		mypy .

.PHONY: _nbval_docker
_nbval_docker:
	pytest --nbval \
		docs/tutorials

.PHONY: nbval
nbval:
	${DOCKER} \
		make _nbval_docker

.PHONY: _docs
_docs:
	cd docs && make html

.PHONY: docs
docs:
	${DOCKER} \
		make _docs

.PHONY: jupyter
jupyter:
	${DOCKER} \
		jupyter notebook --allow-root --ip=0.0.0.0 --NotebookApp.token=''

.PHONY: tests
tests: build_test_containers black sphinx-test pylama mypy nbval lint
	make pytest PYTHON=3.6
	make pytest PYTHON=3.7

.PHONY: lint
lint:
	${DOCKER} \
		poetry run ntc_rosetta lint -i W001 ntc_rosetta/parsers ntc_rosetta/translators

.PHONY: publish
publish:
	@${DOCKER} \
		poetry publish --build --username=$PYPI_USER --password=$PYPI_PASSWORD
