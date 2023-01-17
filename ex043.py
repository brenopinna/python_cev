peso = float(input('Digite seu peso, em kg: '))
altura = float(input('Digite sua altura, em metro: '))
IMC = peso/altura**2
if IMC < 18.5:
    print('Você está ABAIXO DO PESO!')
elif IMC < 25:
    print('Você está no PESO IDEAL!')
elif IMC < 30:
    print('Você possui SOBREPESO!')
elif IMC < 40:
    print('VOcê possui OBESIDADE!')
elif IMC => 40:
    print('Você está no quadro de OBESIDADE MÓRBIDA')