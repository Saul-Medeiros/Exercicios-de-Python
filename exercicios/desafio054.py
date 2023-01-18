"""
Desafio 054 - Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já
são maiores. Considere maior de idade pessoas com 21 anos ou mais.
"""
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pessoa in range(1, 8):
    nasc = int(input(f'Informe o ano de nascimento da {pessoa}ª pessoa: '))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'\n{maior} pessoas são maiores de idade e \n{menor} pessoas ainda não '
      'atingiram a maioridade.')
