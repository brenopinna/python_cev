from random import randint
#faltou o tratamento do input de par ou ímpar
print('=-' * 12)
print('VAMOS JOGAR PAR OU ÍMPAR')
cont = 0
while True:
    pc = randint(1, 10)
    print('=-' * 12)
    user = int(input('Diga um valor: '))
    opcao = input('Par ou Ímpar? [P/I] ').strip()[0]
    soma = user + pc
    print('-' * 24)
    print(f'Você jogou {user} e o computador {pc}. Total de {soma}', end=' ')
    if soma % 2 == 0:
        print('DEU PAR')
        par = True
    else:
        print('DEU ÍMPAR')
        par = False
    print('-' * 24)
    if opcao in 'Pp' and par == True:
        print('VOCÊ VENCEU!\nVamos jogar novamente...')
    elif opcao in 'Ii' and par == False:
        print('VOCÊ VENCEU!\nVamos jogar novamente...')
    else:
        break
    cont += 1
print('VOCÊ PERDEU!')
print('=-' * 12)
print(f'GAME OVER! Você venceu {cont} vezes.')
