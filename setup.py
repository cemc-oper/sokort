from setuptools import setup, find_packages
import codecs
from os import path
import io
import re

with io.open("sokort/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

here = path.abspath(path.dirname(__file__))

with codecs.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


requires_cmadaas = [
    "jinja2"
]

requires_data = [
    "reki"
]

requires_util = [
    "loguru",
]

requires_all = [
    *requires_cmadaas,
    *requires_data,
    *requires_util,
]


setup(
    name='sokort',

    version=version,

    description='CEMC Graphics Script Tool.',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/nwpc-oper/sokort',
    author='perillaroc',
    author_email='perillaroc@gmail.com',

    license='Apache License 2.0',

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    keywords='cemc graph',

    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),

    include_package_data=True,

    package_data={
        '': ["*.ncl", "*.sh"],
    },

    zip_safe=False,

    install_requires=[
        'click',
        'pyyaml',
        "pandas",
        "pillow",
        "IPython",
        "ipywidgets"
    ],

    extras_require={
        "all": requires_all,
        "cmadaas": requires_cmadaas
    }
)
