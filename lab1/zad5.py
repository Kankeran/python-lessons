# Zmień skrypt tak, aby za każdym razem podczas oddania liczby
# program poinformował że podałeś za dużą liczbę lub za małą liczbę

# Rozbudowa pliku zgadywanka.py
# 1. Losujemy więcej liczb.
# 2. Polecenie append() oraz count()
# 1. import random
# 2. ileliczb = int(input("Podaj ilość typowanych liczb: "))
# 3. maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))
# 4. # print("Wytypuj", ileliczb, "z", maksliczba, " liczb: ")
# 5. print("Wytypuj %s z %s liczb: " % (ileliczb, maksliczba))

import random

ileliczb = int(input("Podaj ilość typowanych liczb: "))
maksliczba = input("Podaj maksymalną losowaną liczbę: ")

liczby = []
for i in range(ileliczb):
    liczby.append(random.randint(1, int(maksliczba)))

for k in range(ileliczb):
    print("Zgadnij liczbe numer ", k+1)
    for i in range(6):
        print("proba ", i+1)
        odp = int(input("Jaka liczbe od 1 do " + maksliczba + " wylosowano: "))
        if liczby[k] == odp:
            print("Hura !!!!")
            break
        elif i == 5:
            print("Wylosowana liczba: ", liczby[k])
        elif odp > liczby[k]:
            print("Podales za duza liczbe")
        elif odp < liczby[k]:
            print("Podales za mala liczbe")
        else:
            print("No niestety")
