#!/usr/bin/env python

"""
distutils/setuptools install script.
"""

from setuptools import find_packages, setup

setup(
    name="liquid-sdk",
    version="0.0.1",
    description="An SDK for Security Tooling",
    long_description="An SDK focused on automation for security tooling.",
    author="That Cloud Group",
    url="https://github.com/That-Cloud-Group/liquid",
    scripts=[],
    packages=find_packages(exclude=["tests*"]),
    install_requires=[],
    license="Apache License 2.0",
    python_requires=">= 3.8",
    project_urls={
        "Source": "https://github.com/That-Cloud-Group/liquid",
    },
)
