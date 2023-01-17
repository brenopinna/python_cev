def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
#  Revisar esse, não fui mt bem nesse


print('-' * 30)
n = input('Nome do Jogador: ').strip()
g = input('Número de Gols: ').strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
