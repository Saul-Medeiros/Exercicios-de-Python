"""
Desafio 025 - Crie um programa que leia o nome de uma pessoa e diga se
ela tem "SILVA" no nome.
"""
nome = str(input('Qual é o seu nome completo? ')).strip()
# verifica se tem o nome informado independente de como a pessoa digitar:
print('Seu nome tem Silva?', 'SILVA' in nome.upper())
