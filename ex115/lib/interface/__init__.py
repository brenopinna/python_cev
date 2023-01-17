amarelo = '\033[93m'
azul = '\033[34m'
vermelho = '\033[31m'
verde = '\033[32m'
limpa = '\033[m'


def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return inteiro


def linha(tam=42):
    print('-' * tam)


def titulo(msg):
    linha()
    print(msg.center(42))
    linha()


def menu(*opcoes):
    opcoes = list(opcoes)
    titulo('MENU PRINCIPAL')
    for i, v in enumerate(opcoes):
        print(f'{amarelo}{i + 1}{limpa} - {azul}{v}{limpa}')
    linha()
    resp = leiaInt(f'{amarelo}Sua opção: {limpa}')
    return resp
