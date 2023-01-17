jogadores = []
jogador = {}
while True:
    print('-' * 30)
    nome = input('Nome do Jogador: ')
    qtd = int(input(f'Quantas partidas {nome} jogou? '))
    jogador['nome'] = nome
    jogador['gol'] = []
    jogador['total'] = 0
    for c in range(qtd):
        gols = int(input(f'   Quantos gols na {c + 1}° partida? '))
        jogador['gol'].append(gols)
        jogador['total'] += gols
    jogadores.append(jogador.copy())
    resp = input('Quer continuar? [S/N] ')[0]
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"cod":<4} {"nome":<16}{"gols":<16}total')
print('-' * 42)
for i, j in enumerate(jogadores):
    print(f"{i:>3}{j['nome']:<16}{str(j['gol']):<16}{j['total']}")
while True:
    print('-' * 42)
    cod = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if cod < len(jogadores):
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[cod]["nome"]}')
        for jogo, gol in enumerate(jogadores[cod]['gol']):
            print(f'    No jogo {jogo} fez {gol} gols. ')
    elif cod == 999:
        print('<< VOLTE SEMPRE! >>')
        break
    else:
        print(f'ERRO! Não existe jogador com o código {cod}! Tente novamente')
