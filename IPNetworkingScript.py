import subprocess
import ipaddress

''' alive = []
subnet = ipaddress.ip_network('192.168.1.0/23', strict=False)
for i in subnet.hosts():
    i = str(i)
    retval = subprocess.call(["ping", "-c1", "-n", "-i0.2", "-W1", i])
    if retval == 0:
        alive.append(i)
for ip in alive:
    print(ip + " is alive") ''' 

inputUserIP = input("Enter an IP address to ping:\t")

subInput = "ping -n 1 " + inputUserIP 

subOutput = subprocess.getoutput(subInput)
subOutput = str(subOutput)


print(subOutput)


if "ttl" in subOutput:
    print("ip is up")
else:
    print("ip is down")
