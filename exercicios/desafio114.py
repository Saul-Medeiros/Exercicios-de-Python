"""
Desafio 114 - Crie um código em Python que teste se o site Pudim está acessível
pelo computador usado.
"""
import requests

try:
    # verifica se é possível acessar este site
    requests.get('http://www.pudim.com.br')
# erro de conexão ou url inválida
except ConnectionError:
    print('\033[31mSite do Pudim não está acessível neste computador.\033[m')
# conexão bem sucedida
else:
    print('\033[33mNeste computador é possível acessar o site do Pudim.\033[m')
