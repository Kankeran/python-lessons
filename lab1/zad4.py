# Utwórz grę, w której komputer wybiera losowo słowo, które gracz musi
# odgadnąć. Komputer informuje gracza, ile liter znajduje się w wybranym
# słowie. Następnie gracz otrzymuje pięć szans na zadanie pytania, czy jakaś litera
# jest zawarta w tym słowie. Komputer może odpowiedzieć tylko „tak” lub „nie”.
# Potem gracz musi odgadnąć słowo.

import random

print(
"""
    Witaj w grze 'Zgadnij o jakim slowie mysle'!
 Daję ci 5 szans na znalezienie liter, z których składa się to słowo.
 Wpisujesz wyraz ja sprawdzam czy jakaś literka się zgada i odpowiadam 'tak' lub 'nie'
 Na koniec podajesz to slowo
"""
)

slowa = ("python", "gdansk", "dlaczego", "gdynia", "wsb")
word = random.choice(slowa)
for k in range(0, 5):
    jest = False
    zgaduj = input("Podaj slowo w ktorym uwazasz ze jest zawarta litera: ")
    for i in range(0, len(word)):
        for j in range(0, len(zgaduj)):
            if word[i] == zgaduj[j]:
                jest = True
                break
        if jest:
            print("tak")
            break
    if not jest:
        print("nie")

zgaduj = input("Podaj odpowiedz: ")

if zgaduj == word:
    print("Zgadza się! Zgadłeś!")
else:
    print("Niestety, ta odpowiedź jest zła\nPoprawna to: ", word)

print("Dziękuję za udział w grze.")