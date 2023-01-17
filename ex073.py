times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza',
         'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
         'Atlético-GO', 'Santos', 'Ceará SC', 'Internacional',
         'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude',
         'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
primeiros = times[:5]
ultimos = times[-4:]
ordem = sorted(times)
chape = times.index('Chapecoense')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {primeiros}')
print('-=' * 15)
print(f'Os 4 últimos são {ultimos}')
print('-=' * 15)
print(f'Times em ordem alfabética: {ordem}')
print('-=' * 15)
print(f'O Chapecoense está na {chape + 1}ª posição')
