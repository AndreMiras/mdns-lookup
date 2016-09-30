"""
Verifies core features run as expected.
"""
from __future__ import print_function
import sys
import unittest
from contextlib import contextmanager
from mdnslookup import lookup, format_results
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class TestCore(unittest.TestCase):

    def test_lookup(self):
        """
        Verifies the lookup() function returns a dict as expected.
        """
        hosts_list = [
            # testing one host
            ["raspberrypi.local"],
            # testing two hosts
            ["raspberrypi.local", "whatever.local"],
        ]
        for hosts in hosts_list:
            hosts_ip = lookup(hosts)
            self.assertEqual(len(hosts_ip), len(hosts))
            self.assertEqual(set(hosts_ip.keys()), set(hosts))

    def test_format_results(self):
        """
        Verifies the format_results() correctly prints the results.
        """
        hosts_ip = {
            'raspberrypi.local': '192.168.1.116',
            'whatever.local': None
        }
        with captured_output() as (out, err):
            format_results(hosts_ip)
            output = out.getvalue()
            lines = output.split("\n")
            self.assertTrue(
                'raspberrypi.local' in lines[0])
            self.assertTrue(
                'whatever.local' in lines[1])

if __name__ == '__main__':
    unittest.main()
