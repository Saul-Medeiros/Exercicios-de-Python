"""
Desafio 094 - Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em
uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média.
"""
# lista que irá armazenar as pessoas registradas
grupo = list()
# dicionário que guarda a informação de uma pessoa
pessoa = dict()
# lista que guarda o nome de todas as mulheres registradas
mulheres = list()
# média de idade
media = 0

# Registro de pessoas
while True:
    pessoa.clear()  # limpa os dados registrados no dicionário
    pessoa['nome'] = str(input('Nome: ')).strip()
    # evita sexo informado incorretamente
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    # recebe o acumulativo de idades
    media += pessoa['idade']
    # recebe o nome das mulheres registradas
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    # recebe a cópia do dicionário da pessoa atual
    grupo.append(pessoa.copy())
    # evita resposta informada incorretamente
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, responda apenas S ou N.')
    print('-=' * 30)
    if resp == 'N':
        # para a repetição
        break
# guarda a média de idade de acordo com o acumulativo e o total de
# pessoas registradas
media /= len(grupo)

# Resultado
print(f'''A) O grupo tem {len(grupo)} pessoas.
B) A média de idade é de {media:.2f} anos.
C) As mulheres cadastradas foram: ''', end='')
for m in mulheres:
    print(f'[{m}]', end=' ')
print(f'\nD) Lista das pessoas que estão acima da média:')
# c é apenas uma variável auxiliar para repetição
for c, am in enumerate(grupo):
    if am['idade'] > media:
        print(f'    Nome: {am["nome"]}; Sexo: {am["sexo"]}; '
              f'Idade: {am["idade"]};')
print('<< ENCERRADO >>')
