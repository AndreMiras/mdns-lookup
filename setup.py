#!/usr/bin/env python
import os

from setuptools import setup


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name="mdns-lookup",
    version="20200613",
    description="Python mDNS lookup",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Andre Miras",
    url="https://github.com/AndreMiras/mdns-lookup",
    py_modules=["mdnslookup"],
    scripts=["mdnslookup/mdnslookup.py"],
    entry_points={"console_scripts": ["mdnslookup = mdnslookup:main"]},
    setup_requires=["wheel"],
    install_requires=["dpkt"],
)
