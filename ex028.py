'''from random import randint
#esse fui eu q fiz
segredo = randint(0,5)
user = int(input('Chute um valor: '))
if user == segredo:
    print('ACERTOU!')
else:
    print('ERROU!')'''
from random import randint
from time import sleep
segredo = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
chute = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(1.1)
if segredo == chute:
    print('VOCÊ VENCEU! Eu pensei no número {}.'.format(chute))
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(segredo, chute))
