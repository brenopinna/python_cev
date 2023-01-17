import requests

try:
    requests.get('http://pudim.com.br')
except requests.exceptions.ConnectionError:
    print('\033[1;31mO site Pudim não está acessível no momento.\033[m')
else:
    print('\033[1;93mConsegui acessar o site Pudim com sucesso!\033[m')
