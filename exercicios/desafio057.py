"""
Desafio 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os
valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter
um valor correto.
"""

gen = ['Masculino', 'Feminino']
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
# Enquanto sexo não estiver entre M e F maiúsculo ou minúsculo:
while sexo not in 'MF':
    sexo = str(input('Você não informou o seu sexo corretamente, '
                     'tente novamente: ')).strip().upper()[0]
print('O seu sexo é', end=' ')
# Se sexo estiver entre M maiúsculo ou minúsculo:
if sexo == 'M':
    print(gen[0])
else:
    print(gen[1])
