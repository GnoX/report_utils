#!/usr/bin/env python
from pathlib import Path

from setuptools import find_packages, setup

from report_utils import __version__ as version

requirements = [
    req
    for req in Path("requirements.txt").read_text().splitlines()
    if req and not req.startswith("-")
]

dev_requirements = [
    req
    for req in Path("requirements-dev.txt").read_text().splitlines()
    if req and not req.startswith("-")
]


setup(
    name="report_utils",
    version=version,
    author="gnox",
    url="https://github.com/gnox/report_utils",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    install_requires=requirements,
    python_requires=">=3.6",
    extras_require={"dev": dev_requirements},
    license="MIT",
    packages=find_packages(),
)
