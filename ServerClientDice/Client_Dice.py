from socket import *
import pickle
# Definition der Socket-Parameter
from Tools.scripts.treesync import raw_input

host = "127.0.0.1"  # IP-Adresse des Servers
port = 4711  # Port-Adresse des Servers
addr = (host, port)
buf = 128  # Max. Speicher fuer Eingangsdaten
# Initialisierung eines UDP-Sockets

UDPSock = socket(AF_INET, SOCK_DGRAM)
shutDown = True
while shutDown:
    prompt = raw_input("Geben Sie die gewuenschte Anzahl der Wuerfe ein:>")
    print("Die Eingabe lautet:", prompt)
    shutDown = False

print("Sending to server")
UDPSock.sendto(str(prompt).encode('utf-8'), addr)  # ... versenden
(data, addr) = UDPSock.recvfrom(buf)  # warten...
data = pickle.loads(data)
print()
print("Folgende Augenzahlen wurden geworfen:")
print("( 1er 2er 3er 4er 5er 6er )")
print(" ", data)
print()
# print("Server:", addr, " Nachricht:", int(data))
