ifeq (${PYTHON}, )
override PYTHON=3.8
endif

DOCKER=docker run -t --rm -v ${PWD}:/ntc_rosetta ntc_rosetta-${PYTHON}:latest
JUPYTER=docker run -t --rm -p 8888:8888 -v ${PWD}:/ntc_rosetta ntc_rosetta-${PYTHON}:latest

YANG_VENDORED_BASE_PATH=ntc_rosetta/yang

OPENCONFIG_REPO=https://github.com/networktocode/openconfig.git
OPENCONFIG_BRANCH=7edf3c8
OPENCONFIG_FOLDER=openconfig

NTC_YANG_REPO=https://github.com/networktocode/ntc-yang-models.git
NTC_YANG_BRANCH=3afc611
NTC_YANG_FOLDER=ntc-yang-models

.PHONY: build_test_container
build_test_container:
	docker build \
		--tag ntc_rosetta-${PYTHON}:latest \
		--build-arg PYTHON=${PYTHON} \
		-f Dockerfile .

.PHONY: build_test_containers
build_test_containers:
	make build_test_container PYTHON=3.8
	make build_test_container PYTHON=3.9

.PHONY: enter-container
enter-container:
	${DOCKER} \
		bash

.PHONY: pytest
pytest:
	${DOCKER} \
		pytest --cov=ntc_rosetta --cov-report=term-missing -vvvs ${ARGS}

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
	${JUPYTER} \
		jupyter notebook --allow-root --ip=0.0.0.0 --NotebookApp.token=''

.PHONY: tests
tests: build_test_containers black sphinx-test pylama # Skipping mypy, nbval, lint for now
	make pytest PYTHON=3.8
	make pytest PYTHON=3.9

.PHONY: lint
lint:
	${DOCKER} \
		poetry run ntc_rosetta lint -i W001 -m openconfig ntc_rosetta/parsers/openconfig ntc_rosetta/translators/openconfig
	${DOCKER} \
		poetry run ntc_rosetta lint -i W001 -m ntc ntc_rosetta/parsers/ntc ntc_rosetta/translators/ntc

.PHONY: publish
publish:
	${DOCKER} \
		poetry publish --build --username=$(PYPI_USER) --password="$(PYPI_PASSWORD)"

.PHONY: vendor
vendor:
	rm -rf $(YANG_VENDORED_BASE_PATH)/$(OPENCONFIG_FOLDER)
	git clone $(OPENCONFIG_REPO) $(YANG_VENDORED_BASE_PATH)/$(OPENCONFIG_FOLDER)
	cd $(YANG_VENDORED_BASE_PATH)/$(OPENCONFIG_FOLDER) && git checkout $(OPENCONFIG_BRANCH)
	rm -rf $(YANG_VENDORED_BASE_PATH)/$(OPENCONFIG_FOLDER)/.git

	rm -rf $(YANG_VENDORED_BASE_PATH)/$(NTC_YANG_FOLDER)
	git clone $(NTC_YANG_REPO) $(YANG_VENDORED_BASE_PATH)/$(NTC_YANG_FOLDER)
	cd $(YANG_VENDORED_BASE_PATH)/$(NTC_YANG_FOLDER) && git checkout $(NTC_YANG_BRANCH)
	rm -rf $(YANG_VENDORED_BASE_PATH)/$(NTC_YANG_FOLDER)/.git
