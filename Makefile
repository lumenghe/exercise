.PHONY: clean-pyc
clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	
.PHONY: clean-build	
clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +


.PHONY: clean
clean: clean-build clean-pyc  ## remove all build, test, coverage and Python artifacts


.PHONY: pylint
pylint:
	pylint *.py

.PHONY: flake
flake: ## check style with flake8
	flake8 *.py

.PHONY: format
format:
	isort *.py -l 120
	black --target-version py310 *.py --line-length 120
