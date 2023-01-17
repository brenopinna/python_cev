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
