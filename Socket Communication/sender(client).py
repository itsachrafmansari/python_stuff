import socket as soc

HOST = "127.0.0.1"
PORT = 2000
RECEIVER_ADDRESS = (HOST, PORT)
BUFFER = 1024

UDPSock = soc.socket(soc.AF_INET, soc.SOCK_DGRAM)

while True:
    DATA = input("Send this : ")
    UDPSock.sendto(DATA.encode("utf-8"), RECEIVER_ADDRESS)
    if DATA == "exit":
        break

UDPSock.close()
