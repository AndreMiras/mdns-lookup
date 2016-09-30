#!/usr/bin/env python

from distutils.core import setup

setup(name='mdns-lookup',
      version='20160930',
      description='Python mDNS lookup',
      author='Andre Miras',
      url='https://github.com/AndreMiras/mdns-lookup',
      py_modules=['mdnslookup'],
      scripts=['mdnslookup.py'],
      install_requires=['dpkt'])
