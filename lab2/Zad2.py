# Przygotuj słownik zawierający obce wyrazy oraz ich możliwe znaczenia. Pobierz
# od użytkownika dane w formacie: wyraz obcy: znaczenie1, znaczenie2, ... itd.
# Pobieranie danych kończy wpisanie słowa “koniec”. Podane dane zapisz w pliku.
# Użytkownik powinien mieć możliwość dodawania nowych i zmieniania
# zapisanych danych.


words = input("podaj: ").replace(" ", "").split(":")
key = words[0]
words = words[1].split(",")

print("key = {key} words = {words}".format(key=key, words=words))
