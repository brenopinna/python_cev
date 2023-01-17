n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print("\n-----ESCOLHA SUA OPÇÃO-----")
    opcao = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\nSUA OPÇÃO: '))
    if opcao == 1:
        print(f'\nA soma dos números {n1} e {n2} é {n1 + n2}')
    elif opcao == 2:
        print(f'\nO resultado da multiplicação entre os números {n1} e {n2} é {n1 * n2}')
    elif opcao == 3:
        print(f'\nO maior número entre {n1} e {n2} é {max(n1, n2)}')
    elif opcao == 4:
        n1 = int(input('\nDigite o novo primeiro valor: '))
        n2 = int(input('Digite o novo segundo valor: '))
    elif opcao != 5:
        print('OPÇÃO INVÁLIDA! Digite apenas números entre 1 e 5!')
print('\nOBRIGADO POR USAR O PROGRAMA!')
