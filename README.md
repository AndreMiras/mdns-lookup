# mdns-lookup
Python mDNS lookup

[![Github Actions Tests](https://github.com/AndreMiras/mdns-lookup/workflows/Tests/badge.svg)](https://github.com/AndreMiras/mdns-lookup/actions?query=workflow%3ATests)

This is based on the Stackoverflow answer http://stackoverflow.com/a/35853322/185510.

## Usage
    mdnslookup.py raspberrypi.local hprinter.local
    raspberrypi.local 192.168.1.24
    hprinter.local 192.168.1.42

## Install
Latest stable release:

    pip install https://github.com/AndreMiras/mdns-lookup/archive/master.zip

Development branch:

    pip install https://github.com/AndreMiras/mdns-lookup/archive/develop.zip

## Tests
Using Python unit testing framework:

    python -m unittest discover

Using Tox:

    tox
