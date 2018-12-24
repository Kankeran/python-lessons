# Wykonaj wykres funkcji:
# • f(x) = x/(-3) + a dla x <= 0,
# • f(x) = x*x/3 dla x >= 0,
# • gdzie x = <-10;10> z krokiem 0.5.
# • Współczynnik a podaje
# użytkownik. Na jednym
# wykresie. Wstaw tytuł wykresu,
# nazwy osi, legendę oraz wy
# pozycjonuj osie liczbowe

import matplotlib.pyplot as plt
import numpy as np


def f1(x, a):
    ret = []
    for i in range(len(x)):
        ret.append(x[i]/-3 + a)
    return ret


def f2(x):
    ret = []
    for i in range(len(x)):
        ret.append(x[i]*x[i]/3)
    return ret


a = float(input("Podaj wartosc wspolczynnika przesuniecia: "))
x1 = np.linspace(-10, 0, 11)
x2 = np.linspace(0, 10, 11)
plt.annotate('f(x) = x/(-3) + a', xy=(-5, 5/3 + a), xycoords='data', xytext=(-90, -50), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate('f(x) = x*x/3', xy=(5, 5*5/3), xycoords='data', xytext=(-70, +50), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.plot(x1, f1(x1, a), color='blue')
plt.plot(x2, f2(x2), color='orange')
plt.grid(True)
plt.title('Wykres f(x)')
plt.show()

