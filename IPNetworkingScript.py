#!/usr/bin/env python
#caption = "Hello, World!";
#print( caption );

# Comment type 1
'''
Comment Type 2
'''

'''
Project 1 Network Ping Script.
'''
import subprocess
import ipaddress
# supply IP Address + Subnet (255.255.255.252) or CID Notation /24
import time

user_input = input( "Please enter a Private IP address range: \n examples: \n 10.0.0.0 - 10.255.255.255 \n 172.16.0.0 - 172.31.255.255 \n 192.168.0.0 - 192.168.255.255 \n\n IP Address Range: \t" )
print( "You entered: \n\t" + user_input )










'''
10.0.0.0 - 10.255.255.255
172.16.0.0 - 172.31.255.255
192.168.0.0 - 192.168.255.255
'''

'''
CID Notation = /1 - /32
Subnet Mask = Class A - 255.0.0.0 | Class B - 255.255.0.0 | Class C - 255.255.255.0
'''

'''
PING COMMANDS TO ADD TO SCRIPT:

Windows Pings:
-n count       Number of echo requests to send.
-i TTL         Time To Live.
-r count       Record route for count hops (IPv4-only).
-w timeout     Timeout in milliseconds to wait for each reply.
-S srcaddr     Source address to use.
-c compartment Routing compartment identifier.

Linux Pings:

MacOS Pings:

'''


'''
print("Let's run a function!");

def get_info(  ): #{

    print("This is inside the function");
    user_input - input("What should we say?\n");
    print("Let's Say: \t" + user_input);
#}

#get_info{};

print("This is outside the function!");
'''
