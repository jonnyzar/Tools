#!/bin/bash
#simple ping sweeps

# portscan to discover open ports

if [[ $1 -eq 0 ]];then
    printf "please provide CIDR IP range like so 192.168.178.0/24\n"
    exit 0
fi

if [[ $2 -eq 0 ]];then
    printf "please provide port range like so 1-1024\n"
    exit 0
fi

printf "scanning using nmap...\n"
nc -nv -z -w 2 $1 $2


