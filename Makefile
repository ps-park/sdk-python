help:
	@echo "\033[92m make all      - Run all commands"
	@echo "\033[92m make unittest - Run unit tests"
	@echo "\033[92m make black    - Apply code style fixer"
	@echo "\033[92m make flake8   - Use static analyzing tool to analyze code"

all: unittest black flake8

unittest:
	python -m unittest discover -s tests -p '*_test.py'

black:
	black pspark/ tests/

flake8:
	flake8 pspark/ tests/
