"""
Desafio 042 - Refaça o DESAFIO 035 dos triângulos, acrescentando
o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""

a = float(input('Informe a medida da primeira reta: '))
b = float(input('Informe a medida da segunda reta: '))
c = float(input('Informe a medida da terceira reta: '))

if a < (b + c) and b < (a + c) and c < (a + b):
    print('As três retas informadas formam um triângulo', end=' ')
    if a == b == c:
        print('EQUILÁTERO')
    elif a != b != c:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('As retas informadas não formam um triângulo.')
