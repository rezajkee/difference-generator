# Makefile

build: # собрать пакет
	poetry build


package-install: # установка пакета из ОС (запускать из корня проекта)
	python3 -m pip install --user --force-reinstall  dist/*.whl


lint: # запуск линтера (flake8)
	poetry run flake8 gendiff


test: # запуск pytest
	poetry run pytest


test-coverage: # запись покрытия для CodeClimate
	poetry run pytest --cov=gendiff --cov-report xml


local-test-coverage: # проверка покрытия тестами
	poetry run pytest --cov=gendiff