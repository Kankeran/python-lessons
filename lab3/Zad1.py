# Napisz program, którego
# efektem będzie (patrz w prawo),
# wykres funkcji f(x) = a*x + b,
# gdzie x = <-10;10>, natomiast
# a i b będzie pobierane od
# użytkownika. Na wykresie
# powinna się pokazać informacja
# czy to jest funkcja rosnąca,
# malejąca czy stała

import matplotlib.pyplot as plt
a = int(input("Podaj wartosc wspolczynnika kierunkowego: "))
b = int(input("Podaj wartosc wspolczynnika przesuniecia: "))
x = [-10, 10]
y = [a*x[0]+b, a*x[1]+b]
plt.plot(x, y)
plt.grid(True)
plt.title('Wykres f(x) = a*x + b')
plt.show()

