ePages REST API for Python
==========================

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://github.com/ooz/epages-rest-python

.. image:: https://travis-ci.org/ooz/epages-rest-python.svg?branch=master
    :target: https://travis-ci.org/ooz/epages-rest-python

.. image:: https://badge.fury.io/py/epages-rest-python.svg
    :target: https://badge.fury.io/py/epages-rest-python

------------

See `ePages API <https://developer.epages.com/apps>`_ for detailed documentation.

Installation
------------

Using ``pip``::

    pip install epages-rest-python

Usage
-----

::

    import epages

    api_url = 'https://your.domain.com/rs/shops/yourShopName'
    token = 'yOuRaPiKeYhErE'
    client = epages.RESTClient(api_url,
                               token) # optional for public resources

    # Get the shop information
    shop = client.get('')
    # or
    shop = client.get('/')
    # or
    shop = client.get(api_url)
    print(shop)

    # Create a new product
    payload = {
        'productNumber': '1337'
    }
    new_product = client.post('/products', json=payload)
    print(new_product)

Works with `ePages Now v2 (beyond) shops <https://signup.beyondshop.cloud/>`_, too:

::

    import epages
    client = epages.BYDClient('https://yourshop.beyondshop.cloud/api',
                              'client-id-of-your-app',
                              'client-secret-of-your-app')

    shop = client.get('/shop/shop')

    print(shop['name'])

For more examples see the `epages-rest-python-examples <https://github.com/ooz/epages-rest-python-examples>`_ repository.

Testing
-------

Executing the tests requires a `developer shop <https://developer.epages.com/#modal-popup>`_.

::

    cp run_tests.sh.template run_tests.sh

    # Edit run_tests.sh: enter your ePages API URL and access token

    make test
