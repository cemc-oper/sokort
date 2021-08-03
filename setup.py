from setuptools import setup, find_packages
import io
import re

with io.open("sokort/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name='sokort',

    version=version,

    description='NWPC Graphics Script Tool.',
    long_description=__doc__,

    url='https://github.com/nwpc-oper/sokort',
    author='perillaroc',
    author_email='perillaroc@gmail.com',

    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),

    include_package_data=True,

    package_data={
        '': ["*.ncl", "*.sh"],
    },

    zip_safe=False,

    install_requires=[
        'click',
        'pyyaml',
        "IPython",
        "pillow",
        "pandas",
        "ipywidgets"
    ],

    extras_require={
        "all": {
            "loguru"
        },
        # "jupyter": {
        #     "ipywidgets",
        # }
    }
)
