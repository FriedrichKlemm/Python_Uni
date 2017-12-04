from socket import *

addr = ("127.0.0.1", 4711)  # Server-Adresse
buf = 128  # Max. Speicher fuer Eingangsdaten
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)  # Server an Adresse binden:
while 1:  # er lauscht auf Port 4711
    (data, addr) = UDPSock.recvfrom(buf)  # lauschen..
    if data:
        data = int(data) * 2
        print("Client:", addr, " Nachricht:", data)
        UDPSock.sendto(str(data).encode('utf-8'), addr)
    else:  # Falls 0 Bytes: Abbruch!
        break
UDPSock.close()  # Socket beenden
