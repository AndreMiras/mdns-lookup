# mdns-lookup
Python mDNS lookup

[![Github Actions Tests](https://github.com/AndreMiras/mdns-lookup/workflows/Tests/badge.svg)](https://github.com/AndreMiras/mdns-lookup/actions?query=workflow%3ATests)
[![PyPI version](https://badge.fury.io/py/mdns-lookup.svg)](https://badge.fury.io/py/mdns-lookup)

This is based on the Stackoverflow answer http://stackoverflow.com/a/35853322/185510.

## Usage
Lookup on multiple hostnames:
```sh
mdnslookup raspberrypi.local hprinter.local
```
Output:
```text
raspberrypi.local 192.168.1.24
hprinter.local 192.168.1.42
```

## Install
```sh
pip install mdns-lookup
```

## Tests
```sh
tox
```
