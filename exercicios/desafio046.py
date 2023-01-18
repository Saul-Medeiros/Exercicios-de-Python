"""
Desafio 046 - Faça um programa que mostre na tela uma contagem regressiva para
o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo
entre eles.
"""
from time import sleep
from emoji import emojize
numeros = ['ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO',
           'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ']
for c in range(10, -1, -1):
    print(f'{numeros[c]}')
    sleep(1)
print(emojize(':fireworks::fireworks::fireworks::fireworks::fireworks:',
              language='alias'))
