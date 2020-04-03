#!/usr/bin/env python3

import sys
from setuptools import setup
from setuptools import find_packages


if sys.version_info[:3] < (3, 5):
    raise SystemExit("You need Python 3.5+")

setup(
    name="pystager",
    description="Python staging and logging tool",
    long_description=open("README.md").read(),
    author="Jan Kowalewski",
    url="https://github.com/kowalewskijan",
    download_url="https://github.com/kowalewskijan/pystager.git",
    license="MIT",
    platforms=["Any"],
    keywords="log",
    classifiers=[
        "Topic :: Scientific/Engineering",
        "Environment :: Console",
        "Development Status :: Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    include_package_data=True,
)
