init:
	pip install -r requirements.txt

test:
	@echo "Make sure to set the environment variables:"
	@echo "  EPAGES_HOST"
	@echo "  EPAGES_SHOP"
	@echo "  EPAGES_TOKEN (optional)"
	@python -m unittest discover tests

.PHONY: init test
