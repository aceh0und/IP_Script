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
#  Adding note, because I tested the script for "windows option 1", a random IP that was down, still shows IP is up after it request timed out.
#  Instead of 100% packet loss, it should be a 2nd if/else statment I think.
#  If request time out "IP is Down" | Windows reports "Request timed out" rather than 100% packet loss.
#  If TTL="x" "IP is UP"
#  Great job though, I woke up and was so curious to see what you got done, I jump on and pulled the files and immedately started testing it!


