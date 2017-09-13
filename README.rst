ePages REST API for Python
==========================

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://github.com/ooz/epages-rest-python

.. image:: https://travis-ci.org/ooz/epages-rest-python.svg?branch=master
    :target: https://travis-ci.org/ooz/epages-rest-python

.. image:: https://badge.fury.io/py/epages-rest-python.svg
    :target: https://badge.fury.io/py/epages-rest-python

------------

See ePagesAPI_ for detailed documentation.

Installation
------------

Using ``pip``::

    pip install epages-rest-python

Usage
-----

::

    import epages

    api_url = "https://your.domain.com/rs/shops/yourShopName"
    token = "yOuRaPiKeYhErE"
    client = epages.RESTClient(api_url,
                               token) # optional for public requests

    # Get the shop information
    shop = client.get("") # or client.get("/") or client.get(api_url)
    print(shop)

    # Create a new product
    payload = {
        "productNumber": "1337"
    }
    new_product = client.post("/products", json=payload)
    print(new_product)

Testing
-------

Executing the tests requires a developerShop_.

::

    cp run_tests.sh.template run_tests.sh

    # Edit run_tests.sh: enter your epages host, shop and API key
    
    make test

.. _ePagesAPI: https://developer.epages.com/apps
.. _developerShop: http://www.epages.cloud/developer/
