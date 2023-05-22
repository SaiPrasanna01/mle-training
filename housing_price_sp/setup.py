# import os
import os.path as op
from distutils.core import setup

from setuptools import PEP420PackageFinder

ROOT = op.dirname(op.abspath(__file__))
SRC = op.join(ROOT, "src")

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="housing_price_sp",
    version="0.0.1",
    package_dir={"": "src"},
    description="Housing price prediction",
    long_description=readme,
    author="SAPE SAI PRASANNA",
    author_email="saiprasanna.sape@tigeranalytics.com",
    license=license,
    packages=PEP420PackageFinder.find(where=str(SRC)),
)
