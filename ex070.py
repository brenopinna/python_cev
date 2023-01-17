print('-' * 35)
print('{:^35}'.format('LOJA SUPER BARATÃO'))
print('-' * 35)
total = 0
produtoscaros = 0
nomebarato = 'nenhum'
valorbarato = 0
cont = 0
while True:
    while True:
        nome = input('Nome do Produto: ').strip().title()
        if nome not in ' ':
            break
    while True:
        try:
            preco = float(input('Preço: R$'))
            break
        except ValueError or preco not in ' ':
            continue
    if preco > 1000:
        produtoscaros += 1
    if preco < valorbarato or cont == 0:
        valorbarato = preco
        nomebarato = nome
    cont += 1
    total += preco
    while True:
        opcao = input("Quer continuar? [S/N] ").strip().upper()
        if opcao in 'SN':
            try:
                opcao = opcao[0]
                break
            except IndexError:
                continue
    if opcao == 'N':
        break
    else:
        continue
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'''O total da compra foi R${total:.2f}
Temos {produtoscaros} produtos custando mais de R$1000.00
O produto mais barato foi {nomebarato} que custa R${valorbarato:.2f}''')
