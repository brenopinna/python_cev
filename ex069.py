adultos = 0
homens = 0
mulheresnovas = 0
#melhorar o tratamento das respostas (usar while not in...)
while True:
    print('-' * 25)
    print('{:^25}'.format('CADASTRE UMA PESSOA'))
    print('-' * 25)
    while True:
        try:
            idade = int(input('Idade: '))
            break
        except ValueError:
            continue
    while True:
        sexo = input('Sexo: [M/F] ').strip().upper()
        if sexo in 'MF':
            try:
                sexo = sexo[0]
            except IndexError:
                continue
            break
        else:
            continue
    if idade > 18:
        adultos += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresnovas += 1
    print('-' * 25)
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
        if opcao in 'NS':
            try:
                opcao = opcao[0]
            except IndexError:
                continue
            break
        else:
            continue
    if opcao == 'S':
        continue
    elif opcao == 'N':
        print('\n====== FIM DO PROGRAMA ======')
        print(f'Total de pessoas com mais de 18 anos: {adultos}')
        print(f'Ao todo temos {homens} homens cadastrados')
        print(f'E temos {mulheresnovas} mulheres com menos de 20 anos')
        break
