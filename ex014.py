celsius = float(input('\033[31mInforme a temperatura em °C: '))
fahrenheit = (celsius*9/5)+32
print('\033[36mA temperatura de \033[32m{} °C\033[36m corresponde a \033[32m{} °F\033[m!'.format(celsius,fahrenheit))