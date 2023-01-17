from random import randint
from time import sleep
from operator import itemgetter  # Coisa nova, nunca tinha visto
jogadores = {}
ordem = {}  # Eu nao tinha feito assim, usei uma lista mas ficou mt gambiarrento
print('Valores sorteados: ')
for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 6)
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
ordem = sorted(jogadores.items(), key=itemgetter(1), reverse=True)  #0 seria a chave, e 1 é o valor dessa chave
for i, v in enumerate(ordem):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
