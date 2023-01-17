from interface import *
from arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu('Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema')
    if resp == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resp == 2:
        # Opção de cadastrar uma nova pessoa.
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        # Opção de sair do sistema.
        titulo('Saindo do Sistema... Até logo!')
        break
    else:
        # Digitou uma opção errada no menu.
        print(f'\033[31mERRO: Digite uma opção válida!\033[m')
    sleep(1.5)
