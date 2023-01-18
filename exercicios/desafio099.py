"""
Desafion 099 - Faça um programa que tenha uma função chamada maior(), que
receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep


# Pontos de carregamento "..." mostrado em intervalos
def dotinterval():
    sleep(1)
    for c in range(0, 3):
        print('.', end='')
        sleep(1)
    print()


# Desempacotamento de parâmetro
def maior(* num):
    print('-=' * 30)
    print('Analisando os valores passados', end='')
    dotinterval()
    lista = list()
    print('Valores informados: ', end=' ')
    for n in num:
        lista.append(n)
        print(n, end=' ')
    print()
    # ordena os valores passados para a lista
    lista.sort()
    if len(num) > 0:
        print(f'O maior entre os {len(num)} números informados é {lista[-1]}.')
    else:
        print('O maior valor informado é 0.')


maior(5, 4, 3, 2, 8, 9)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
