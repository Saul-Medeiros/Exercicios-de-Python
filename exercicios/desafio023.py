"""
Desafio 023 - Faça um programa que leia um número de 0 a 9999 e
mostre na tela cada um dos dígitos separados.

Ex:
Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar 1
"""
n = int(input('Informe um número: '))
print('\n' + '-'*4, 'NÚMERO', n, '-'*4)
# divisão inteira por 1 e pega o resto da divisão por 10 (último número):
print('Unidade: {}'.format(n // 1 % 10))
# divisão inteira por 10 e pega o resto da divisão por 10 (penúltimo número):
print('Dezena: {}'.format(n // 10 % 10))
# divisão inteira por 100 e pega o resto da divisão por 10 (segundo número):
print('Centena: {}'.format(n // 100 % 10))
# divisão inteira por 1000 e pega o resto da divisão por 10 (primeiro número):
print('Milhar: {}'.format(n // 1000 % 10))
