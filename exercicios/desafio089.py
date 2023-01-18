"""
Desafio 089 - Crie um programa que leia nome e duas notas de vários alunos e
guarde tudo em uma lista composta. No final, mostre um boletim contendo a média
de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente.
"""
from time import sleep
boletim = []
cont = 0  # contador auxiliar
while True:
    boletim.append(list())  # adiciona uma lista dentro da lista boletim
    boletim[cont].append(str(input('Nome: ')).strip().title())
    boletim[cont].append(float(input('Nota 1: ')))
    boletim[cont].append(float(input('Nota 2: ')))
    boletim[cont].append((boletim[cont][1] + boletim[cont][2]) / 2)
    resp = ' '  # redefine a resposta a cada loop
    # resposta informado incorretamente (caso não for a primeira vez)
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    print('-=' * 14)
    if resp == 'N':
        break
    cont += 1
print('No. NOME           MÉDIA')
print('-' * 28)
# mostrando boletim dos alunos
for indice, aluno in enumerate(boletim):
    print(f'{indice:<3} {aluno[0]:<16}{aluno[3]}')
print('-' * 38)
# mostrando notas individuais
while True:
    # redefine a escolha a cada loop para entrar no loop interno
    escolha = -1
    # caso escolha seja maior que as opções (exceto 999), ou menor que 0
    while escolha < 0 or (escolha != 999 and escolha > cont):
        escolha = int(input('Mostrar as notas de qual '
                            'aluno? (999 interrompe): '))
    if escolha == 999:
        break
    else:
        print(f'Notas de {boletim[escolha][0]} são [{boletim[escolha][1]}, '
              f'{boletim[escolha][2]}]')
        print('-' * 38)
print('\nFinalizando...\n')
sleep(3)
print('<<< Volte Sempre >>>')
