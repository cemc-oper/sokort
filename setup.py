from setuptools import setup

import sys
sys.path.insert(0, ".")

import versioneer

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass()
)
