# Napisz program, który pobierze
# od użytkownika ilość ruchów
# jaką ma wykonać cząstka, a
# następnie narysuje
# wygenerowane losowo ruch tej
# cząstki
#
# Cząsteczka, której ruch będziemy śledzić, znajduje się w początku układu
# współrzędnych (0, 0);
# • w każdym ruchu cząsteczka przemieszcza się o stały wektor o wartości 1;
# • kierunek ruchu wyznaczać będziemy losując kąt z zakresu <0; 2  >;
# • współrzędne kolejnego położenia cząsteczki wyliczać będziemy ze wzorów:
# x[n] = x[n-1] + r * cos(k)
# y[n] = y[n-1] + r * sin(k)
# • – gdzie: r – długość jednego kroku, – kąt wskazujący kierunek ruchu w
# odniesieniu do osi OX.
# • końcowy wektor przesunięcia obliczymy ze wzoru: |s| = sqrt(𝑥2 + 𝑦2)

import matplotlib.pyplot as plt
import numpy as np
import random


def f1(num):
    retx = [0]
    rety = [0]
    for i in range(num):
        radian = (random.randint(0, 360) * np.pi) / 180
        retx.append(retx[i] + (1 * np.cos(radian)))
        rety.append(rety[i] + (1 * np.sin(radian)))
    return [retx, rety]


a = int(input("Podaj ilosc krokow czasteczki: "))
x, y = f1(a)
plt.plot(x, y, color='green')
plt.grid(True)
plt.title('Ruchy Browna')
plt.show()
