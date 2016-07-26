#!/usr/bin/env python

import os
import re
import sys
from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

setup(
    name='epages-rest-python',
    version='0.1.0',
    url='https://github.com/ooz/epages-rest-python',
    author='Oliver Zscheyge',
    description='The epages online shop API for Python',
    long_description=read('README.rst'),
    license='MIT',
    author_email='oliverzscheyge@gmail.com',
    packages=['epages'],
    package_data={'': ['README.rst', 'LICENSE'], 'scripts': ['callback.py']},
    data_files = ["README.rst"],
    include_package_data=True,
    install_requires=['requests==2.10.0'],
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    )
)
