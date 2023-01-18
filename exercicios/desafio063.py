"""
Desafio 063 - Escreva um programa que leia um número n inteiro qualquer e
mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""

n = int(input('Informe um número: '))
c = 1
t1 = 0  # primeiro termo
t2 = 1  # segundo termo
print('\033[1m~'*56 + f'\n{"SEQUÊNCIA DE FIBONACCI":^56}\n' + '~'*56 + '\033[m')
while c <= n:
    if c % 13 == 0:
        print()
    print(f'\033[1;33m{t1}', end=' → ')
    t3 = t1 + t2  # terceiro termo equivalente a soma dos dois anteriores
    t1 = t2  # t1 passa a valer o termo seguinte
    t2 = t3  # t2 passa a valer o último termo
    c += 1
print('FIM\033[m\n' + '\033[1m~'*56)
