preco = float(input('Insira o preço padrão do produto: R$'))
dinheiro = int(input('[1] Dinheiro/Cheque\n[2] Cartão\nOPÇÃO: '))
if dinheiro == 1:
    print('Você selecionou a opcao "Dinheiro/Cheque"')
    print('O valor a ser pago é de R${:.2f}'.format(preco - (preco * 0.1)))
elif dinheiro == 2:
    print('Você selecionou a opcao "Cartão"')
    modo = int(input('[1] À vista\n[2] Parcelado'))
    if modo == 1:
        print('O valor a ser pago é de R${:.2f}'.format(preco - (preco * 0.05)))
    elif modo == 2:
        parcelas = int(input('Digite em quantas parcelas deseja dividir: '))
        if parcelas <= 2:
            print('O valor a ser pago é de R${:.2f}'.format(preco))
        else:
            print('O valor a ser pago é de R${:.2f}'.format(preco * 1.2))
