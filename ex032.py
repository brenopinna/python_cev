from datetime import date
ano = int(input('Digite um ano (0 para analisar o ano atual): '))
if ano == 0:
    ano = date.today().year # pega o ano atual da máquina
if (ano % 4) == 0 and ano % 100 != 0 or ano % 400 == 0:#ano bissexto: - divisível por 4
    print(f'O ano {ano} é BISSEXTO')                                # - se for multiplo de 100, deve ser de 400 tbm
else:
    print(f'O ano {ano} NÃO é BISSEXTO')