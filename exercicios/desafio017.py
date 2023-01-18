# Desafio 017 - Faça um programa que leia o comprimento do cateto
# oposto e do cateto adjacente e de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa.

from math import hypot  # importação de função que calcula a hipotenusa
from math import sqrt  # adiciona a importação de sqrt da classe math

# Usando math hypot
co = float(input('Informe a medida do cateto oposto: '))
ca = float(input('Agora, informe a medida do cateto adjacente: '))
h = hypot(co, ca)
print(f'''{co} é o comprimento do cateto oposto, {ca} o comprimento do cateto
adjacente e {h:.2f} é o comprimento da hipotenusa.''')

# Usando math pow:
h = pow(co, 2) + pow(ca, 2)
print(f'''{co} é o comprimento do cateto oposto, {ca} o comprimento do cateto
adjacente e {h:.2f} é o comprimento da hipotenusa.''')

# Calculo sem importação:
h = (co ** 2 + ca ** 2) ** (1 / 2)
print(f'''{co} é o comprimento do cateto oposto, {ca} o comprimento do cateto
adjacente e {h:.2f} é o comprimento da hipotenusa.''')
