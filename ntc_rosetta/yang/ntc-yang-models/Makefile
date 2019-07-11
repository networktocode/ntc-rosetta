BASE=models/
OC_PYANG_PLUGINS_DIR="/src/oc-pyang/openconfig_pyang/plugins"

MODELS_DOC_PATH=docs/models/dynamic

CTR=docker run --rm -v $(PWD):/ntc-yang-models ntc-models-builder

.PHONY: build-container
build-container:
	docker build --no-cache -t ntc-models-builder -f Dockerfile .

.PHONY: tree
tree:
	$(CTR) yangson -p $(shell find models/* -type d | xargs | sed 's/ /:/g') -t models/ntc-models-library.json

.PHONY: tests
tests:
	$(CTR) pytest -v

.PHONY: _docs
_docs:
	cd docs && make html

.PHONY: docs
docs:
	$(CTR) make _docs

.PHONY: build-model-doc
build-model-doc:
	pyang \
		--plugindir $(OC_PYANG_PLUGINS_DIR) \
		-f docs \
		--path models \
		--doc-format rst \
		--strip-ns \
		models/$(MODEL)/*.yang > $(MODELS_DOC_PATH)/$(MODEL).rst

.PHONY: pyang-help
pyang-help:
	$(CTR) pyang \
		--plugindir $(OC_PYANG_PLUGINS_DIR) \
		--help

.PHONY: lint
lint:
	$(CTR) pyang \
		--plugindir $(OC_PYANG_PLUGINS_DIR) \
		--path models \
		--doc-format html \
		--doc-title="NTC YANG models" \
		--allowed-prefixes=ntc \
		--openconfig \
		models/*/*.yang
