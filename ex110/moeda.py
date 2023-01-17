def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')


def aumentar(valor, taxa, formata=False):
    res = valor + (valor * taxa / 100)
    return res if not formata else moeda(res)


def diminuir(valor, taxa, formata=False):
    res = valor - (valor * taxa / 100)
    return res if not formata else moeda(res)


def dobro(valor, formata=False):
    res = valor * 2
    return res if not formata else moeda(res)


def metade(valor, formata=False):
    res = valor / 2
    return res if not formata else moeda(res)


def resumo(valor, aumento, reducao):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))  # Centraliza o texto em 30 caracteres
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')  # Esse \t é tabulação, é como apertar "tab"
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento:02}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{reducao:02}% de redução: \t{diminuir(valor, reducao, True)}')
