# Przygotuj słownik zawierający obce wyrazy oraz ich możliwe znaczenia. Pobierz
# od użytkownika dane w formacie: wyraz obcy: znaczenie1, znaczenie2, ... itd.
# Pobieranie danych kończy wpisanie słowa “koniec”. Podane dane zapisz w pliku.
# Użytkownik powinien mieć możliwość dodawania nowych i zmieniania
# zapisanych danych.


menu = """Menu Akcji:
1. Pokaz zawartosc slownika
2. Szukaj wyrazu w slowniku
3. Zmien znaczenie podanego wyrazu
4. Dodaj nowy wyraz do slownika
Wpisz \"Koniec\" aby wyjsc z programu"""

slownik = open("Dictionary.klswh", "a+", encoding='utf-8')


def pobierzSlowoIZnaczenia(linia):
    linia = linia.replace(" ", "").replace("\n", "").split(":")
    linia[1] = linia[1].split(",")
    return linia


def pokazSlownik():
    slownik.seek(0)
    for linia in slownik:
        slowo, znaczenia = pobierzSlowoIZnaczenia(linia)
        print("key = {key} words = {words}".format(key=slowo, words=znaczenia))


def szukajSlowa():
    slownik.seek(0)
    szukaneSlowo = input("wprowadz slowo ktorego szukasz: ")
    for linia in slownik:
        slowo, znaczenia = pobierzSlowoIZnaczenia(linia)
        if szukaneSlowo == slowo:
            slownik.seek(0, 2)
            print("key = {key} words = {words}".format(key=slowo, words=znaczenia))
            return
    print("Nie znaleziono slowa")


def zmienZnaczenie():
    words = input("podaj: ").replace(" ", "").split(":")
    key = words[0]
    words = words[1].split(",")

    print("key = {key} words = {words}".format(key=key, words=words))


def dodajSlowo():
    slowa = input("podaj: ").replace(" ", "")
    slownik.writelines(slowa + "\n")


funkcje = [
    None,
    pokazSlownik,
    szukajSlowa,
    zmienZnaczenie,
    dodajSlowo
]

while True:
    print(menu)
    wybor = input("Wybierz Akcje: ")
    if wybor == "Koniec" or wybor == "koniec":
        break
    if not wybor.isdigit() or 1 > int(wybor) or 4 < int(wybor):
        continue
    funkcje[int(wybor)]()
    # except ValueError:
    #     print("Wartosc musi byc cyfra")
    # except IndexError:
    #     continue

slownik.close()
