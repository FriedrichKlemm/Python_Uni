from random import randint

LIMIT = 600  # Anzahl der Wuerfe
Nclass = 6  # Anzahl der "Wuerfeloberflaechen"
i = 0  # Initialisierungen
erg = 0
mittel = 0
schwank = 0
sqrt_erg = 0
wuerfel = [0, 0, 0, 0, 0, 0]


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
