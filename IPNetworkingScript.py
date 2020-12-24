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

print("Windows = 1\nOSX = 2\nLinux = 3")
inputUserOS = input("What Operating System Are you running?:     ")
inputUserOS = int(inputUserOS)

if inputUserOS == 1:
    packetTag = "-n"
elif inputUserOS == 2:
    packetTag = "-c"
elif inputUserOS == 3:
    packetTag = "-c"
else:
    print("This is not an option!!")



inputUserIP = input("Enter an IP address to ping:     ")
inputUserPacketNum = input("How many packets would you like to send?:     ")

inputUserPacketNum = str(inputUserPacketNum)

subInput = "ping " + packetTag + " " + inputUserPacketNum + " " + inputUserIP 
# Change subInput so that the user can input a number they would like rather than use 1.  :)

subOutput = subprocess.getoutput(subInput)
subOutput = str(subOutput)


print(subOutput)


if "100% packet loss" in subOutput:
    print("Ip is down")
else:
    print("Ip is up")



