init:
	pipenv --three
	pipenv install requests
	pipenv install six
	pipenv install --dev pytest

init2:
	pipenv --two
	pipenv install requests
	pipenv install six
	pipenv install --dev pytest

test:
	@pipenv run pytest \
	|| (echo "Test(s) failed. Did you install the requirements and set the \
	environment variables (run_tests.sh.template)?")

.PHONY: init init2 test
