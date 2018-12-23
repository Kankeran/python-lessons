# Napisz program, który liczy za użytkownika. Umożliw użytkownikowi
# wprowadzenie liczby początkowej, liczby końcowej i wielkości odstępu między kolejnymi
# liczbami.

poczatek = int(input("Podaj liczbę początkową: "))
koniec = int(input("Podaj liczbę końcową: "))
skok = int(input("Podaj po ile ma dodwać: "))
liczby = [poczatek]
while liczby[-1] <= (koniec - skok):
    liczby.append(liczby[-1] + skok)
print(liczby)