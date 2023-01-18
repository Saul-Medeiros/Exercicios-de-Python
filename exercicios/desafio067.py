"""
Desafio 067 - Faça um programa que mostre a tabuada de vários números, um de
cada vez, para cada valor digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo.
"""
from time import sleep
while True:
    n = int(input('Informe um valor [valor negativo encerra o programa]: '))
    if n < 0:
        break
    print('='*24 + f'\n  TABUADA DO NÚMERO {n}\n' + '='*24)
    for c in range(1, 11):
        produto = n * c
        print(f'{n} x {c:2} = {produto}')
    print('='*22)
    sleep(1)  # 1 segundo de espera
print('Programa encerrado. Tenha um bom dia!')
