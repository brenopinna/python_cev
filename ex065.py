maior = menor = cont = soma = opcao = 0
while opcao != 2:
    num = int(input('\nDigite um número inteiro: '))
    if num > maior or cont == 0:
        maior = num
    if num < menor or cont == 0:
        menor = num
    cont += 1
    soma += num
    media = soma / cont
    opcao = int(input('Deseja continuar a inserir valores?\n[1] Sim\n[2] Não\nOPÇÃO: '))
print(f'\nO maior valor inserido foi {maior}')
print(f'O menor valor inserido foi {menor}')
print(f'A média de todos os {cont} valores inseridos foi {media}\n')
print('\nOBRIGADO POR USAR O PROGRAMA!')
