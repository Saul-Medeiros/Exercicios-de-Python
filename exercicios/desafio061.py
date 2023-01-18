"""
Desafio 061 - Refaça o DESAFIO 051, lendo o primero termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
cont = 0
ordinais = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto',
            'Sexto', 'Sétimo', 'Oitavo', 'Nono', 'Décimo']
while cont < 10:
    print(f'{ordinais[cont]} termo: {termo}')
    termo += razao
    cont += 1
