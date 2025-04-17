help:
	@echo "\033[92m make all    - Run all commands"
	@echo "\033[92m make flake8 - Use static analyzing tool to analyze code"

all: flake8

flake8:
	flake8
