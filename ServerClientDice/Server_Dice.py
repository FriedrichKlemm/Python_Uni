from random import randint
from socket import *
import pickle


def sqrt(a):  # Berechnung der Quadratwurzel
    i = -1
    quadrat = 0

    if a < 0:
        print("sqrt: negatives Argument")
        return -1

    while quadrat < a:
        i += 1
        quadrat = i * i

    sqrt_erg = i
    return sqrt_erg


addr = ("127.0.0.1", 4711)  # Server-Adresse
buf = 128  # Max. Speicher fuer Eingangsdaten
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)  # Server an Adresse binden:
while 1:  # er lauscht auf Port 4711
    (data, addr) = UDPSock.recvfrom(buf)  # lauschen..
    if data:
        LIMIT = int(data)  # Anzahl der Wuerfe
        Nclass = 6  # Anzahl der "Wuerfeloberflaechen"
        i = 0  # Initialisierungen
        erg = 0
        mittel = 0
        schwank = 0
        sqrt_erg = 0
        wuerfel = [0, 0, 0, 0, 0, 0]

        # Wuerfeln ...
        i = 0
        while i < LIMIT:
            erg = randint(1, 6)
            wuerfel[erg - 1] += 1
            i += 1

        # Ausgabe Wuerfelergebnis
        print()
        print("Folgende Augenzahlen wurden geworfen:")
        print("( 1er 2er 3er 4er 5er 6er )")
        print(" ", wuerfel)
        print()

        # Bestimmung der erlaubten Schwankung
        mittel = LIMIT / Nclass
        schwank = sqrt(mittel)
        print("Kontrolle:")
        print(" Theoret. Bereich = ", mittel, "+/-", schwank)
        print()
        print("Client:", addr, " Nachricht:", data)

        data = pickle.dumps(wuerfel)
        UDPSock.sendto(data, addr)
    else:  # Falls 0 Bytes: Abbruch!
        break
UDPSock.close()  # Socket beenden
