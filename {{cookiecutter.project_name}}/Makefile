include $(CURDIR)/config.mk
VERSION=0.0.1

ROOT_DIR:=$(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))
VENV=$(ROOT_DIR)/venv
flake8=$(VENV)/bin/flake8
pip=$(VENV)/bin/pip3
pytest=$(VENV)/bin/pytest
bandit=$(VENV)/bin/bandit
black=$(VENV)/bin/black
python=$(VENV)/bin/$(PYTHON)
coverage=$(VENV)/bin/coverage

$(VENV):
	$(PYTHON) -m venv $(VENV)

$(VENV)/bin/$(PKG_NAME): $(VENV)
	$(pip) install .

venv: $(VENV)

install: $(VENV)/bin/$(PKG_NAME)

dev-env:
	cp scripts/pre-commit.sh .git/hooks/

dev-install: dev-env $(pytest)
	$(pip) install -e .

$(pytest): $(VENV)
	$(pip) install .[dev]

lint: $(pytest)
	$(black) $(PKG_NAME)
	$(flake8) $(PKG_NAME)

test: $(pytest)
	$(pytest) -v --cov-branch --cov=tests/unit --cov-report=term
	$(coverage) report -m --fail-under=50

scan:
	$(bandit) -r app/

run:
	./scripts/entrypoint.sh

clean:
	rm -rf $(VENV)
	rm -rf $(PKG_NAME).egg-info
	rm -rf dist
	rm -rf build
	find . -type d -name __pycache__ -delete
	find . -name '*.pyc' -delete

docker-start-dev-env:
	docker build -t $(PROJECT_NAME) .
	docker run --entrypoint /bin/sh -v $(CURDIR):/src --name $(PROJECT_NAME)-dev-env -itd $(PROJECT_NAME)
	docker exec $(PROJECT_NAME)-dev-env pip3 install -e .[dev]
	docker attach $(PROJECT_NAME)-dev-env

docker-stop-dev-env:
	docker stop $(PROJECT_NAME)-dev-env
	docker rm $(PROJECT_NAME)-dev-env

docker-build:
	docker build -t $(PROJECT_NAME):$(VERSION) .

docker-run:
	docker run -p --name $(PROJECT_NAME) -td $(PROJECT_NAME):$(VERSION)
	docker ps -l

docker-stop:
	docker stop $(PROJECT_NAME)

docker-remove:
	docker rmi -f $(PROJECT_NAME)
