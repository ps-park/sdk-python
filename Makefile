help:
	@echo "\033[92m make all    - Run all commands"
	@echo "\033[92m make black  - Apply code style fixer"
	@echo "\033[92m make flake8 - Use static analyzing tool to analyze code"

all: black flake8

black:
	black .

flake8:
	flake8 .
