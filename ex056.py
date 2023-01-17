totidade = 0
maioridadehomem = 0
nomevelho = ''
novas = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    totidade += idade
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome.capitalize()
    if sexo == 'F' and idade < 20:
        novas += 1
medidade = totidade / 4
print(f'A média de idade do grupo é de {medidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {novas} mulheres com menos de 20 anos.')
