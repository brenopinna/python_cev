from random import choice

print('Digite o n_completo dos 4 lista para o sorteio: ')
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('ALuno 4: ')
alunos = [a1, a2, a3, a4]
aluno = choice(alunos)
print('O aluno escolhido para apagar o quadro foi {}!'.format(aluno))
