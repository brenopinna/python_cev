print('=='*14)
print('\033[36mCONVERSOR DE BASES NUMÉRICAS\033[m')
print('=='*14)
num = int(input('Digite o número a ser convertido: '))
print('Selecione sua opcao:\033[33m\n[1] BINÁRIO\n[2] OCTAL\n[3] HEXADECIMAL\033[m')
opcao = int(input('OPÇÃO: '))
if opcao == 1:
    print('O número \033[34m{}\033[m, convertido para uma base binária, equivale a \033[32m{}\033[m'.format(num, bin(num)[2:]))
elif opcao == 2:                                                                                                #aqui é um fatiamento de string
    print('O número \033[34m{}\033[m, convertido para uma base octal, equivale a \033[32m{}\033[m'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número \033[34m{}\033[m, convertido para uma base hexadecimal, equivale a \033[32m{}\033[m'.format(num, hex(num)[2:]))
else:
    print('\033[31mDIGITE APENAS 1, 2 ou 3!\033[m')
