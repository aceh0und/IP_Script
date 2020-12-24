#!/usr/bin/env python

'''
Project 1 Network Ping Script.
IPNetworkingScript - Created By Ace & Akuma
'''
import subprocess
import ipaddress
import time
# supply IP Address + Subnet (255.255.255.252) or CID Notation /24

user_input = input( "Please enter a Private IP address range: \n examples: \n 10.0.0.0 - 10.255.255.255 \n 172.16.0.0 - 172.31.255.255 \n 192.168.0.0 - 192.168.255.255 \n\n IP Address Range: \t" )

print( " You entered: \t\t" + user_input + "\n\n")

# Add if/else statement here to output the wrong typed output that doesn't match the examples.

user_input = input( "Please enter a CIDR or Subnet Mask Address for Network: \n examples: \n CIDR Notation: /1 - /32 \n Subnet Mask: A.B.C.D \n\n CIDR or Subnet Mask: \t" )
print( " You entered: \t\t" + user_input )

# Add if/else statement here to output the wrong typed output that doesn't match the examples.







'''
if "ttl" in subOutput:
    print("ip is up")
else:
    print("ip is down")
'''

'''
Apply read scrolling text to script in order to have a "load type screen" to allow process to be run in the back and then outputted afterwards.
import time
string = 'hello world'
for char in string:
    print char
    time.sleep(.25)
'''


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
-c count        Stop after sending (and receiving) count ECHO_RESPONSE packets.  If this option is not specified, ping will operate until interrupted.  If this option is specified in conjuction with ping sweeps, each sweep will consist of count packets.
-m ttl          Set the IP Time To Live for outgoing packets.  If not specified, the kernel uses the value of the net.inet.ip.ttl MIB variable.
-o              Exit succcessfully after receiving one reply packet.

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
