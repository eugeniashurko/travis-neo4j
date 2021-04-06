import os
from setuptools import setup, find_packages


setup(
    name="package",
    version="0.1",
    description="la",
    packages=find_packages(),
    python_requires=">=3.6",
    setup_requires=[
        "setuptools_scm",
    ],
    install_requires=[
        "neo4j",
    ],
    extras_require={
        "dev": [
            "tox", "pytest", "pytest-bdd", "pytest-cov==2.10.1",
            "pytest-mock==3.3.1", "codecov",
            "neo4j"
        ],
    }
)
