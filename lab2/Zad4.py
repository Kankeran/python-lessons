# Napisz program, który na podstawie danych pobranych od użytkownika, czyli
# długości boków, sprawdza, czy da się zbudować trójkąt i czy jest to trójkąt
# prostokątny. Jeżeli da się zbudować trójkąt, należy wydrukować jego obwód i
# pole, w przeciwnym wypadku komunikat, że nie da się utworzyć trójkąta.

import math

wymiary = list(map(int, input("Podaj wymiary trujkata oddzielone litera 'x': ").replace(" ", "").split("x")))
wymiary.sort(reverse=True)

if len(wymiary) != 3 or wymiary[0] > wymiary[1] + wymiary[2]:
    print("Z tego nie da się utworzyc trojkata")
    exit(0)

if pow(wymiary[0], 2) == pow(wymiary[1], 2) + pow(wymiary[2], 2):
    print("Trojkat jest trojkatem prostokatnym")

obwod = wymiary[0] + wymiary[1] + wymiary[2]
pole = obwod/2
pole = math.sqrt(pole*(pole-wymiary[0])*(pole-wymiary[1])*(pole-wymiary[2]))

print("Obwod trojkata: {0}\nPole trojkata: {1}".format(obwod, round(pole, 2)))
