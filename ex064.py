num = cont = soma = 0
while num != 999:
    num = int(input('Digite um número inteiro: '))
    if num != 999:
        cont += 1
        soma += num
print(f'A soma dos {cont} números digitados é {soma}')
