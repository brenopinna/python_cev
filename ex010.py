dinheiro = float(input('\033[33mQuanto dinheiro em reais você tem?\033[m '))
dolar = round(dinheiro/3.27, 2)
print('\033[34mCom o valor de \033[32mR${:.2f}\033[m, \033[34mvocê pode comprar \033[35mUS${:.2f}.\033[m'.format(dinheiro, dolar))
