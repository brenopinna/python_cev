import datetime
usuario = int(input('Digite seu ano de nascimento: '))
hoje = datetime.date.today().year
idade = hoje - usuario
if idade == 18:
    print('É hora de se alistar ao serviço militar!')
elif idade < 18:
    print('Ainda faltam {} ano(s) para o seu alistamento.'.format(18 - idade))
elif idade > 18:
    print('Ops! Você deveria ter se alistado a {} ano(s)!'.format(idade - 18))
