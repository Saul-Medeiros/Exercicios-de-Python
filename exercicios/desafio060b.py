"""
Desafio 060 - Faça um programa que leia um número qualquer e mostre o seu
fatorial usando for.
Ex: 5! = 5x4x3x2x1 = 120
"""
from math import factorial
n = int(input('Informe um número: '))
txt = ''
for c in range(n, 0, -1):
    txt += f'{c} x ' if c > 1 else f'{c} ='
print('\033[1m-=' * 7, f'FATORIAL DE {n}', '-=' * 7 + '\033[m')
print(f'{n}! =', end=' ')
print(factorial(n) if n < 2 else f'{txt} {factorial(n)}')
print('\033[1m-=' * 22 + '\033[m')
