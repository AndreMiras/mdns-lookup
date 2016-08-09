#!/usr/bin/env python
"""
#DNS(qd=[Q(name='hprinter.local')]) hprinter.local
#DNS(qd=[Q(name='pvknoppix.local')]) pvknoppix.local
#DNS(qd=[Q(name='microknoppix.local')]) microknoppix.local
#DNS(qd=[Q(name='esp01.local')]) esp01.local
#DNS(an=[RR(name='esp01.local', rdata='\n\x00\x00\x04', ttl=120, cls=32769)], op=33792) esp01.local 10.0.0.4
#DNS(an=[RR(name='PVknoppix.local', rdata='\n\x00\x00\xc2', ttl=120, cls=32769)], op=33792) PVknoppix.local 10.0.0.194
"""
import socket
import struct
from dpkt.dns import DNS, DNS_A
UDP_IP="0.0.0.0"
UDP_PORT=5353
MCAST_GRP = '224.0.0.251'
sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind( (UDP_IP,UDP_PORT) )
#join the multicast group
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
for host in ['esp01','microknoppix','pvknoppix','hprinter'][::-1]:
    # the string in the following statement is an empty query packet
    dns = DNS('\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01')
    dns.qd[0].name=host+'.local'
    sock.sendto(dns.pack(), (MCAST_GRP, UDP_PORT))
sock.settimeout(5)
while True:
    try:
        m = sock.recvfrom(1024)
        # print '%r'%m[0],m[1]
        dns = DNS(m[0])
        if len(dns.qd)>0:
            print dns.__repr__(),dns.qd[0].name
        if len(dns.an)>0 and dns.an[0].type == DNS_A:
            print dns.__repr__(), dns.an[0].name, socket.inet_ntoa(dns.an[0].rdata)
    except socket.timeout:
        break
