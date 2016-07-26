epages REST API for Python
==========================

See epagesAPI_ for detailed documentation.

Installation
------------

Using ``pip``::

    pip install epages-rest-python

Usage
-----

::

    import epages

    client = epages.HTTPClient("https://your.domain.com/rs/shops/yourShopName",
                               "yOuRaPiKeYhErE")
    shop = client.get("") # or client.get("/")
    print(shop)

    params = {

    }

    payload = {
        "productNumber": "1337"
    }
    new_product

Testing
-------

Executing the tests requires a developerShop_.

::

    cd epages-rest-python
    cp run_tests.sh.template run_tests.sh
    # Edit run_tests.sh: enter your epages host, shop and API key
    bash run_tests.sh

Contributing
------------

TODO

.. _epagesAPI: https://developer.epages.com/apps
.. _developerShop: http://www.epages.cloud/developer/
