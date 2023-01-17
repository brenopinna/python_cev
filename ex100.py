from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando 5 valores da lista:', end=' ')
    for c in range(5):
        num = randint(1, 10)
        lista.append(num)
        print(num, end=' ')
        sleep(0.23)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista}, temos {soma}.')


numeros = []
sorteia(numeros)
somaPar(numeros)
