from setuptools import setup, find_packages
import io
import re

with io.open("nwpc_graphics/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name='nwpc-graphics',

    version=version,

    description='NWPC Graphics project.',
    long_description=__doc__,

    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),

    include_package_data=True,

    package_data={
        '': ["*.ncl", "*.sh"],
    },

    zip_safe=False,

    install_requires=[
        'click',
        'pyyaml',
        "pytimeparse",
        "IPython",
        "loguru",
        "pillow"
    ],

    entry_points={
        "console_scripts": [
            "nwpc_graphics = nwpc_graphics._main:cli",
        ],
    },
)
