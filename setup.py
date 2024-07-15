"""Python setup.py for ulta3 package"""

import io
import os
from setuptools import find_packages, setup
from ulta3 import __version__


def read(*paths, **kwargs):
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="ulta3",
    version=__version__,
    description="ulta3 ",
    url="https://github.com/vladtara/ulta3/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Vlad Tara",
    packages=find_packages(where="ulta3"),
    install_requires=read_requirements("requirements.txt"),
    author_email="vlad@glaps.fun",
    license="MIT",
    entry_points={"console_scripts": ["ulta3 = ulta3:cli"]},
)
