"""
Desafio 030 - Crie um programa que leia um número inteiro e mostre
na tela se ele é PAR ou ÍMPAR.
"""
print('-=-' * 4, 'PROGRAMA PAR OU ÍMPAR', '-=-' * 4)
n = int(input('Me informe um número inteiro qualquer: '))
if n % 2 == 0:  # resto da divisão por 2 = 0
    print('O número {} é PAR!'.format(n))
else:  # resto da divisão por 2 = 1
    print('O número {} é ÍMPAR!'.format(n))
