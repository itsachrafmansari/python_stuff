import socket as soc

HOST = ""
PORT = 2000
ADDRESS = (HOST, PORT)
BUFFER = 1024

UDPSock = soc.socket(soc.AF_INET, soc.SOCK_DGRAM)
UDPSock.bind(ADDRESS)

while True:
    RECEIVED_DATA, SENDER_ADDRESS = UDPSock.recvfrom(BUFFER)
    print(f"Client {SENDER_ADDRESS[0]}:{SENDER_ADDRESS[1]} sent {RECEIVED_DATA.decode('utf-8')}")
    if RECEIVED_DATA == "exit":
        break
UDPSock.close()
