pessoa = dict()
pessoas = list()
soma_idd = 0
while True:
    pessoa['nome'] = input('Nome: ')
    while True:  #input e verificação do sexo
        pessoa['sexo'] = input('Sexo: [M/F] ').upper()[0]
        if pessoa['sexo'] in "MF":
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma_idd += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True:  #input e verificação da opção de continuar ou não
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in "SN":
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = soma_idd/len(pessoas)
print(f'B) A média de idade é de {media}')
print(f'C) As mulheres cadastradas foram', end=' ')
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        print(pessoa["nome"], end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for pessoa in pessoas:
    if pessoa['idade'] > media:
        print(end='    ')
        for k, v in pessoa.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')
