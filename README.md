[![Actions Status](https://github.com/rezajkee/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/rezajkee/python-project-lvl2/actions)
[![lint and test](https://github.com/rezajkee/python-project-lvl2/actions/workflows/lint_and_test.yml/badge.svg)](https://github.com/rezajkee/python-project-lvl2/actions/workflows/lint_and_test.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/98d14f5e4c4063e5909c/maintainability)](https://codeclimate.com/github/rezajkee/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/98d14f5e4c4063e5909c/test_coverage)](https://codeclimate.com/github/rezajkee/python-project-lvl2/test_coverage)

## Difference generator

##### Второй учебный проект Hexlet

##### Данный пакет используется для выявления отличий между двумя файлами
##### форматов JSON или YAML

##### В пакете реализованы 3 вида представления отличий: stylish, plain, json
```bash
usage: gendiff [-h] [-f {stylish,plain,json}] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f {stylish,plain,json}, --format {stylish,plain,json}
                        set format of output (stylish by default)
```
##### Пример использования stylish формата с "плоскими" файлами JSON:
[![asciicast](https://asciinema.org/a/aKRDOmFHDwN2cu1yrNhc2T86A.svg)](https://asciinema.org/a/aKRDOmFHDwN2cu1yrNhc2T86A)
##### Пример использования stylish формата с файлами JSON с рекурсивной структурой:
[![asciicast](https://asciinema.org/a/tWeljN5IiSS4lGir8GfXN0aCF.svg)](https://asciinema.org/a/tWeljN5IiSS4lGir8GfXN0aCF)
##### Пример использования plain формата с файлами JSON с рекурсивной структурой:
[![asciicast](https://asciinema.org/a/7OiICFBCyPRhsvJaBTRXxBmAW.svg)](https://asciinema.org/a/7OiICFBCyPRhsvJaBTRXxBmAW)
##### Пример использования json формата с файлами JSON с рекурсивной структурой:
[![asciicast](https://asciinema.org/a/1F0UB4Uy7Tr55HvkWL1Cz9Hwe.svg)](https://asciinema.org/a/1F0UB4Uy7Tr55HvkWL1Cz9Hwe)

##### Для установки пакета с GitHub с помощью pip используйте
```bash
$ pip install git+https://github.com/rezajkee/python-project-lvl2.git
```