VERSION=0.1.1
PACKAGE=gendiff

create-venv: # Настройка окружения
	@pip install -r ./requirements.txt
	@uv venv --python=python3.10

build: # Сборка проекта
	@echo "Building package..."
	uv build

package-install:
	@echo "Installing package: $(PACKAGE)-$(VERSION)-py3-none-any.whl"
	@echo "To override installation please type: make package-install PACKAGE=name:string VERSION=version:string"
	@uv tool install dist/$(PACKAGE)-$(VERSION)-py3-none-any.whl

install: create-venv build package-install

package-reinstall: build
	uv tool install --force dist/*.whl

test:
	uv run pytest

lint:
	uv run ruff check

check: test lint

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml