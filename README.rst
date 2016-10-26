ePages REST API for Python
==========================

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
    client = epages.HTTPClient(api_url,
                               "yOuRaPiKeYhErE")

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

    cd epages-rest-python
    cp run_tests.sh.template run_tests.sh
    # Edit run_tests.sh: enter your epages host, shop and API key
    bash run_tests.sh

Contributing
------------

TODO

.. _ePagesAPI: https://developer.epages.com/apps
.. _developerShop: http://www.epages.cloud/developer/
