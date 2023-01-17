jogador = dict()
jogador['nome'] = input('Nome do Jogador: ')
jogador['gols'] = list()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for cont in range(1, partidas + 1):
    qtd = int(input(f'   Quantos gols na {cont}ª partida? '))
    jogador['gols'].append(qtd)
jogador['total'] = sum(jogador['gols'])
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na {i + 1}ª partida, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
