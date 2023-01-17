alunos = []
aluno = []
notas = []
while True:
    nome = input('Nome: ')
    p1 = float(input('Nota 1: '))
    p2 = float(input('Nota 2: '))
    media = f'{(p1 + p2) / 2:.1f}'
    notas.append(p1)
    notas.append(p2)
    aluno.append(nome)
    aluno.append(notas[:])
    aluno.append(media)
    alunos.append(aluno[:])
    notas.clear()
    aluno.clear()
    op = input('Quer continuar? [S/N] ')
    if op in 'Nn':
        print('-=' * 30)
        print(f'No. NOME{" " * 9}MÉDIA')
        print('-' * 24)
        for i, v in enumerate(alunos):
            print(i, end='   ')
            print(f'{alunos[i][0]:15}', end='')
            print(f'{alunos[i][2]}')
        break
while True:
    print('-' * 33)
    index = int(input(f'Mostrar notas de qual aluno? (999 interrompe): '))
    if index == 999:
        print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')
        break
    print(f'Notas de {alunos[index][0]} são {alunos[index][1]}')
