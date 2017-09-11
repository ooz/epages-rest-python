init: install_pipenv
	pipenv --three
	make install_dependencies

init2: install_pipenv
	pipenv --two
	make install_dependencies

install_pipenv:
	pip install pipenv

install_dependencies:
	pipenv install requests
	pipenv install six
	pipenv install --dev pytest

test:
	pipenv run pytest

# Travis CI
ci_install:
	pip install requests
	pip install six
	pip install pytest

ci_script:
	pytest

.PHONY: init init2 install_pipenv install_dependencies test \
ci_install ci_script
