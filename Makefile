init:
	pip install -r requirements.txt

test:
	@python -m unittest discover tests \
	|| (echo "Tests failed. Did you set the environment variables EPAGES_API_URL \
	and EPAGES_TOKEN?")

.PHONY: init test
