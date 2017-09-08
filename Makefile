init:
	pipenv --three
	pipenv install requests
	pipenv install six
	pipenv install pytest --dev

init2:
	pipenv --two
	pipenv install requests
	pipenv install six
	pipenv install pytest --dev

test:
	@pipenv run python -m unittest discover tests \
	|| (echo "Tests failed. Did you install the requirements and set the \
	environment variables EPAGES_API_URL and EPAGES_TOKEN?")

.PHONY: init init2 test
