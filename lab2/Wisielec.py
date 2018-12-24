import random
slowa = ("python","gdansk","dlaczego","gdynia","wsb")
word = random.choice(slowa)
#print (word)
poprawnie = word
pomie =""
while word:
position = random.randrange(len(word))
pomie += word[position]
word = word[:position] + word[(position + 1):]
print (pomie)
Gra – odgadnij słowo
print(
"""
Witaj w grze 'Wymieszane litery'!
Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez
podawania odpowiedzi.)
"""
)
print("Zgadnij, jakie to słowo:", pomie)
zgaduj = input("\nTwoja odpowiedź: ")
while zgaduj != poprawnie and zgaduj != "":
print("Niestety, to nie to słowo.")
zgaduj = input("Twoja odpowiedź: ")
if zgaduj == poprawnie:
print("Zgadza się! Zgadłeś!\n")
print("Dziękuję za udział w grze.")
Import słów z pliku
with open("slowa.txt", "r") as f:
linie= f.readlines()
Ilosc_lini = len(linie)
rand_linia = random.randint(0,
ilość_lini)
SLOWO = linie[rand_linia-1].strip()
• Otwieramy plik, zawartość
umieszczamy w zmiennej f
• Czytamy wszystkie linie
• Sprawdzamy ilość linii
• Losujemy linie tzn. słowo
• Metoda strip () - Usuwa białe
znaki lub znak podanny jako char
z początku i końca napisu

MAX_POMYLKA = len(ludz) – 1 # ilość pomyłek
slowa = (”MORZE", ”BALTYK", ”GDYNIA", ”SLASKA", "PYTHON") #
przykładowa krotka słów
slowo = random.choice(slowa) # losowo wybierane słowo z krotki
dlugosc_slowa = "-" * len(slowo) #sprawdzenie dlugosci słowa i
zastąpienie go kreskmi
POMYLKA = 0 # liczba nietrafionych liter
uzyte = [] # litery już użyte w zgadywaniu
Pętla główna
print("Witaj w grze ’Wisielec'. Powodzenia!")
while POMYLKA < MAX_POMYLKA and dlugosc_slowa != slowo:
print(ludz[POMYLKA])
print("\nWykorzystałeś już następujące litery:\n", uzyte)
print("\nNa razie zagadkowe słowo wygląda tak:\n", dlugosc_slowa)
zgadnij = input("\n\nWprowadź literę: ")
zgadnij = zgadnij.upper() # zamiana na duże litery wprowadzonych
liter
Sprawdzanie czy litera nie była już użyta przez
gracza i wymuszenie podania innej
while zgadnij in uzyte:
print("Już wykorzystałeś literę", zgadnij)
zgadnij = input("Wprowadź literę: ")
zgadnij = zgadnij.upper()
uzyte.append(zgadnij)
Sprawdzenie i Zapamiętanie odgadniętej litery
w zmiennej nowa, zwiększenie pomyłki o 1
if zgadnij in slowo:
print("\nTak!", zgadnij, "znajduje się w zagadkowym słowie!")
nowa = ""
for i in range(len(slowo)):
if zgadnij == slowo[i]:
nowa += zgadnij
else:
nowa += dlugosc_slowa[i]
dlugosc_slowa = nowa
else:
print("\nNiestety,", zgadnij, "nie występuje w zagadkowym słowie.")
POMYLKA += 1
THE END
if POMYLKA == MAX_POMYLKA:
print(ludz[POMYLKA])
print("\nZostałeś powieszony!")
else:
print("\nOdgadłeś!")
print("\nZagadkowe słowo to", slowo)