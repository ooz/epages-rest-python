init:
	pip install -r requirements.txt

test:
	# Make sure the environment variables are set!
	ifndef EPAGES_HOST
    $(error EPAGES_HOST is undefined)
	endif
	ifndef EPAGES_SHOP
    $(error EPAGES_SHOP is undefined)
	endif
	ifndef EPAGES_TOKEN
    $(error EPAGES_TOKEN is undefined)
	endif
	# Execute all tests
	@python -m unittest discover tests

.PHONY: init test
