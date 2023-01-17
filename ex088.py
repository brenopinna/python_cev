from random import randint
from time import sleep
temp = []
jogos = []
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
while len(jogos) < qtd:
    while len(temp) < 6:
        num = randint(1, 60)
        if num not in temp:
            temp.append(num)
    jogos.append(temp[:])
    temp.clear()
print(f'-=-=-=  SORTEANDO {qtd} JOGOS  -=-=-=')
for i, v in enumerate(jogos):
    print(f'Jogo {i + 1}: {v}')
    sleep(1)
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')
