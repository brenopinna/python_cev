def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        eleitor = 'NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        eleitor = 'VOTO OPCIONAL'
    else:
        eleitor = 'VOTO OBRIGATÓRIO'
    return f'Com {idade} anos: {eleitor}'


print('-' * 30)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
