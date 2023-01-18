"""
Desafio 016 - Crie um programa que leia um número Real qualquer pelo
teclado e mostre na tela a sua porção inteira.
Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
"""
from math import floor  # adiciona a importação da função floor do pacote math
from math import trunc  # adiciona a importação da função trunc do pacote math

# Método floor:
n = float(input('Digite um número: '))
print('O número {} tem a parte Inteira {}'.format(n, floor(n)))
# floor arrendonda para baixo

# Método trunc:
print('O número {} tem a parte Inteira {}'.format(n, trunc(n)))
# trunc elimina as casas decimais

# Transformando em int:
print('O número {} tem a parte Inteira {}'.format(n, int(n)))
# int converte o número float para inteiro, assim eliminando
# as suas casas decimais
