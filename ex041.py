import datetime
hoje = datetime.date.today().year
niver = int(input('Digite seu ano de nascimento: '))
idade = hoje - niver
if idade <= 9:
    print('CATEGORIA: \033[31mMIRIM\033[m')
elif idade<= 14:
    print('CATEGORIA: \033[36mINFANTIL\033[m')
elif idade <= 19:
    print('CATEGORIA: \033[31mJÚNIOR\033[m')
elif idade <= 25:
    print('CATEGORIA: \033[35mSÊNIOR\033[m')
elif idade > 25:
    print('CATEGORIA: \033[33mMASTER\033[m')



