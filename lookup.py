#!/usr/bin/env python
"""
Python lookup module and program.
Inspired from the stackoverflow answer:
http://stackoverflow.com/a/35853322/185510
"""
from __future__ import print_function
import argparse
import socket
import struct
from dpkt.dns import DNS, DNS_A


def lookup(hosts):
    UDP_IP = "0.0.0.0"
    UDP_PORT = 5353
    MCAST_GRP = '224.0.0.251'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((UDP_IP, UDP_PORT))
    # join the multicast group
    mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    for host in hosts:
        # the string in the following statement is an empty query packet
        dns = DNS(
                '\x00\x00\x01\x00\x00\x01\x00\x00' +
                '\x00\x00\x00\x00\x00\x00\x01\x00\x01')
        dns.qd[0].name = host
        sock.sendto(dns.pack(), (MCAST_GRP, UDP_PORT))
    sock.settimeout(5)
    while True:
        try:
            m = sock.recvfrom(1024)
            # print '%r'%m[0],m[1]
            dns = DNS(m[0])
            if len(dns.qd) > 0:
                print(dns.__repr__(), dns.qd[0].name)
            if len(dns.an) > 0 and dns.an[0].type == DNS_A:
                print("%s %s %s" % (
                        dns.__repr__(),
                        dns.an[0].name,
                        socket.inet_ntoa(dns.an[0].rdata)))
        except socket.timeout:
            break


def main():
    """
    Parses sys args and calls the lookup function.
    """
    parser = argparse.ArgumentParser(description='Performs mDNS lookups.')
    parser.add_argument(
            'hosts', nargs='+', help='Hosts to resolve')
    args = parser.parse_args()
    hosts = args.hosts
    lookup(hosts)

if __name__ == "__main__":
    main()
