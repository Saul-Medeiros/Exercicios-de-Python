"""
Desafio 020 - O mesmo professor do desafio anterior quer sortear a
ordem de apresentação de trabalhos dos alunos. Faça um programa que
leia  o nome dos quatro alunos e mostre a ordem sorteada.
"""
# importação da função de embaralhamento
from random import shuffle
nome1 = input('Informe o nome do 1° aluno: ')
nome2 = input('Informe o nome do 2° aluno: ')
nome3 = input('Informe o nome do 3° aluno: ')
nome4 = input('Informe o nome do 4° aluno: ')
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)  # embaralha os componentes dentro da lista
print('A ordem de apresentação será {}'.format(lista))
