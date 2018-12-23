# Popraw program Wymieszane litery tak, żeby każdemu słowu towarzyszyła
# podpowiedź. Gracz powinien mieć możliwość zobaczenia podpowiedzi, jeśli
# utknie w martwym punkcie. Dodaj system punktacji, który nagradza graczy
# rozwiązujących anagram bez uciekania się do podpowiedzi.

import random

slowa = ("python", "gdansk", "dlaczego", "gdynia", "wsb")
podpowiedzi = {
    'python': "jezyk w którym napisany jest ten program",
    'gdansk': "jedno z miast trojmiasta",
    'dlaczego': "pytajnik powodu",
    'gdynia': "najmłodsze miasto trójmiasta",
    'wsb': "uczelnia w której powstał ten program"
}
pkt = 10
word = random.choice(slowa)
podpowiedz = podpowiedzi[word]
poprawnie = word
pomie = ""
while word:
    position = random.randrange(len(word))
    pomie += word[position]
    word = word[:position] + word[(position+1):]

print("""
    Witaj w grze 'Wymieszane litery'!
 Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby uzyskać podpowiedź wpisz '/podpowiedź'.)
(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
"""
)
print("Zgadnij jakie to słowo:", pomie)

uzylPodpowiedzi = False
zgaduj = input("\nTwoja odpowiedź: ")
while zgaduj != poprawnie and zgaduj != "":
    if zgaduj == "/podpowiedź":
        pkt -= 4 if pkt - 4 >= 0 else pkt
        uzylPodpowiedzi = True
        print("podpowiedź: ", podpowiedz)
        zgaduj = input("Twoja odpowiedź: ")
        continue
    pkt -= 1 if pkt - 1 >= 0 else pkt
    print("Niestety, to nie to słowo")
    if uzylPodpowiedzi:
        print(podpowiedz)
    zgaduj = input("Twoja odpowiedź: ")
if zgaduj == poprawnie:
    print("Zgadza się! Zgadłeś!\nOtwrzymujesz %d pkt" %pkt)
print("Dziękuję za udział w grze.")
