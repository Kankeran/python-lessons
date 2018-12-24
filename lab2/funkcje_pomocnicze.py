import math


def srednia(list):
    sum = 0
    for item in list:
        sum += item
    return sum/len(list)


def mediana(list):
    listLen = len(list)
    if listLen % 2 == 0:
        return (list[int(listLen/2)] + list[int((listLen/2)+1)]) / 2
    return list[int((listLen+1)/2)]


def odchylenie_standardowe(list):
    sred = srednia(list)
    odchylenie = 0
    for item in list:
        odchylenie += pow(item-sred, 2)
    return math.sqrt(odchylenie)
