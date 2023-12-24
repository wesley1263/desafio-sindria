# Created by Weslei Souza

COLOUR_GREEN=\033[0;32m
COLOUR_RED=\033[0;31m
COLOUR_BLUE=\033[0;34m
COLOUR_END=\033[0m


run-app:
	@echo "${COLOUR_BLUE}Running app in debug mode...${COLOUR_END}"
	@uvicorn src.main:app --reload

formatter:
	@black .
	@isort .
	@flake8
	@autoflake --remove-all-unused-imports --remove-unused-variables --recursive --in-place --ignore-init-module-imports .
