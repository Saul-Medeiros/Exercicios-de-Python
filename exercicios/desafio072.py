"""
Desafio 072 - Crie um programa que tenha uma tupla totalmente preend=chida com
uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por
extenso.
"""

cardinais = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',\
    'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',\
    'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if n > 20 or n < 0:
            print('Tente novamente.', end=' ')
        else:
            break
    print(f'Você digitou o número {cardinais[n]}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
