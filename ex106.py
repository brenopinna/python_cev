from time import sleep
cores = (
    '\033[m',    # 0 - limpa
    '\033[41m',  # 1 - vermelho
    '\033[42m',  # 2 - verde
    '\033[43m',  # 3 - amarelo
    '\033[44m',  # 4 - azul
    '\033[45m',  # 5 - roxo
    '\033[7m'    # 6 - branco
)  # Revisar essa aqui, fiz certo mas poderia ser melhor, refazer


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'{msg:^{tam}}')
    print('~' * tam)
    print(cores[0], end='')
    sleep(1)


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = input('Função ou Biblioteca> ')
    if comando.lower() == 'fim':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)

