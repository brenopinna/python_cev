vel = float(input('Velocidade: '))
if vel > 80:
    print('Você foi multado em R${:.2f}'.format((vel - 80)*7))
else:
    print('Você não foi multado. Tenha um bom dia!')
