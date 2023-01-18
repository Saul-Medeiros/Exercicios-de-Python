"""
Desafio 060 - Faça um programa que leia um número qualquer e mostre o seu
fatorial usando while.
Ex: 5! = 5x4x3x2x1 = 120
"""
n = int(input('Informe um número: '))
c = n  # maior número
fat = 1  # 0! = 1
txt = ''
while c >= 1:
    fat *= c
    if c > 1:
        txt += '{} x '.format(c)  # n x ... x 2 x
    c -= 1
print('\033[1m-=' * 7, f'FATORIAL DE {n}', '-=' * 7 + '\033[m')
print(f'{n}! =', end=' ')
if n == 1 or n == 0:
    print(fat)
else:
    print(f'{txt}1 = {fat}')  # ...x 1 =
print('\033[1m-=' * 22 + '\033[m')
