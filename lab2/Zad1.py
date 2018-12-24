# Napisz program, który umożliwi wprowadzanie ocen z podanego przedmiotu,
# następnie policzy i wyświetla średnią, medianę i odchylenie standardowe
# wprowadzonych ocen. Funkcje pomocnicze i statystyczne umieść w osobnym
# module.

import lab2.funkcje_pomocnicze as func

przedmioty = ["matematyka", "historia", "fizyka", "polski"]
oceny = {}
for przedmiot in przedmioty:
    oceny[przedmiot] = []
    while True:
        ocena = input("Podaj kolejna ocene do przedmiotu " + przedmiot + ": ")
        if ocena == "":
            break
        oceny[przedmiot].append(int(ocena))
    oceny[przedmiot].sort()

for przedmiot in przedmioty:
    if len(oceny[przedmiot]) == 0:
        print("brak ocen dla przedmiotu: " + przedmiot)
        continue
    print(
        "Srednia ocen przedmiotu "
        + przedmiot
        + " wynosi: "
        + str(func.srednia(oceny[przedmiot]))
    )
    print(
        "Mediana ocen przedmiotu "
        + przedmiot
        + " wynosi: "
        + str(func.mediana(oceny[przedmiot]))
    )
    print(
        "Odchylenie standardowe ocen przedmiotu "
        + przedmiot
        + " wynosi: "
        + str(func.odchylenie_standardowe(oceny[przedmiot]))
    )
    print(oceny[przedmiot])
