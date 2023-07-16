# import os
import os.path as op
from setuptools import setup, Extension

from setuptools import PEP420PackageFinder

ROOT = op.dirname(op.abspath(__file__))
SRC = op.join(ROOT, "src")

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="housing_price_sp_final",
    version="0.0.2",
    package_dir={"": "src"},
    description="Housing price prediction",
    long_description=readme,
    author="SAPE SAI PRASANNA",
    author_email="saiprasanna.sape@tigeranalytics.com",
    license=license,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    packages=PEP420PackageFinder.find(where=str(SRC)),
    url="https://github.com/SaiPrasanna01/mle-training"
)
