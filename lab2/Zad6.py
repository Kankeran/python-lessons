# Pobierz od użytkownika n liczb i zapisz je w liście. Wydrukuj:
# 1. elementy listy i ich indeksy,
# 2. elementy w odwrotnej kolejności,
# 3. posortowane elementy.
# 4. Usuń z listy pierwsze wystąpienie elementu podanego przez użytkownika.
# 5. Usuń z listy element o podanym indeksie.
# 6. Podaj ilość wystąpień oraz indeks pierwszego wystąpienia podanego elementu.
# 7. Wybierz z listy elementy od indeksu i do j.


def elementyListy(lista):
    for i in range(len(lista)):
        print("Index {0} Element {1}".format(i, lista[i]))


def elementyListyOdwrotnie(lista):
    print(lista[::-1])


def posortowaneElementyListy(lista):
    posortowanaLista = lista.copy()
    posortowanaLista.sort()
    print(posortowanaLista)


def usunPierwszeWystapienie(lista):
    element = int(input("Podaj element, ktory chcesz usunac: "))
    lista.remove(element)


def usunPodIndeksem(lista):
    index = int(input("Podaj indeks elementu, ktory chcesz usunac: "))
    lista.pop(index)


def iloscElementow(lista):
    element = int(input("Podaj element, ktorego dane chcesz sprawdzic: "))
    print(
        "Indeks pierwszego wystapienia: {0}\nIlosc wystapien {1}".format(
            lista.index(element),
            lista.count(element)
        )
    )


def elementyPrzedzialu(lista):
    przedzial = list(
        map(
            int,
            input(
                "Podaj przedzial, ktory chcesz zobaczyc (liczby oddzielone dwukropkiem): "
            ).replace(" ", "")
            .split(":")
        )
    )
    print(lista[przedzial[0]:przedzial[1]])


lista = list(map(int, input("Podaj dowolna ilosc liczb oddzielonych spacjami: ").split()))
funkcje = [
    None,
    elementyListy,
    elementyListyOdwrotnie,
    posortowaneElementyListy,
    usunPierwszeWystapienie,
    usunPodIndeksem,
    iloscElementow,
    elementyPrzedzialu
]
menu = """Menu Akcji:
1. Pokaz elementy listy i ich indeksy
2. Pokaz elementy listy w odwrotnej kolejnosci
3. Pokaz posortowane elementy
4. Usun z listy pierwsze wystapienie podanego elementu
5. Usun z listy element o podanym indeksie
6. Pokaz ilosc wystapien oraz indeks pierwszego wystapienie podanego elementu
7. Pokaz elementy listy z podanego przedzialu
0. Wyjdz"""

while True:
    try:
        print(menu)
        wybor = int(input("Wybierz Akcje: "))
        if wybor == 0:
            break
        funkcje[wybor](lista)
    except ValueError:
        print("Wartosc musi byc cyfra")
