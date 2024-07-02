# If you have not used make before then checkout the following link:
#    https://www.gnu.org/software/make/manual/html_node/
.PHONY: clean \
	test build venv \
	lint

VENV_BIN_PATH=./venv/bin

all: lint
clean:
	rm -rf $(PWD)/build
	rm -rf $(PWD)/dist

venv: ./venv/bin/activate

./venv/bin/activate: requirements.txt
	test -d ./venv || python -m venv ./venv
	./venv/bin/activate; pip install --upgrade pip; pip install -Ur requirements.txt; pip install -Ur requirements-dev.txt
	touch ./venv/bin/activate

test: venv
	$(VENV_BIN_PATH)/pytest

lint: venv
	$(VENV_BIN_PATH)/black ./liquid/
	$(VENV_BIN_PATH)/pylint ./liquid/

build: venv
	python -m build
