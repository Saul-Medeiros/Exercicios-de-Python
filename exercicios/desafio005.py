"""
Desafio 005 - Faça um programa que leia um número Inteiro e mostre na tela o
seu sucessor e seu antecessor.
"""
n1 = int(input('Informe um número: '))
print('Analisando o número {}, seu antecessor é o numero {} e seu sucessor é '
      'o número {}'.format(n1, (n1 - 1), (n1 + 1)))
