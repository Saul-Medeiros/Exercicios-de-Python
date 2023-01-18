"""
Desafio 019 - Um professor quer sortear um dos seus quatro alunos
para apagar o quadro. Faça um programa que ajude ele, lendo o nome
deles e escrevendo o nome do escolhido.
"""
# importação da função choice do pacote random
from random import choice
nome1 = input('Informe o nome do 1° aluno: ')
nome2 = input('Informe o nome do 2° aluno: ')
nome3 = input('Informe o nome do 3° aluno: ')
nome4 = input('Informe o nome do 4° aluno: ')
# [] armazena uma lista com variáveis
lista = [nome1, nome2, nome3, nome4]
# choice escolhe uma variável aleatória dentro de uma lista
escolhido = choice(lista)
print('O escolhido para apagar o quadro foi o {}'.format(escolhido))
