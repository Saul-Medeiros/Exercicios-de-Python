"""
Desafio 084 - Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
dados = []
pesado = leve = cont = 0
while True:
    dados.append(list())  # adiciona uma lista interna em dados
    # cadastro da lista interna
    dados[cont].append(str(input('Nome: ')).strip().title())
    dados[cont].append(float(input('Peso: ')))
    if cont == 0:
        pesado = leve = dados[cont][1]
    else:
        # Preenchimento de lista do mais leve
        if dados[cont][1] < leve:
            leve = dados[cont][1]
        # Preenchimento de lista do mais pesado
        if dados[cont][1] > pesado:
            pesado = dados[cont][1]
    resp = ' '  # redefine o valor de resp a cada repetição
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break  # finaliza a repetição
    cont += 1
print(f'{len(dados)} pessoas foram cadastradas.')
print(f'O menor peso foi {leve}kg, das pessoas ', end='')
# para cada lista em dados
for pessoa in dados:
    if pessoa[1] == leve:
        print(f'[{pessoa[0]}] ', end='')
print()
print(f'O maior peso foi {pesado}kg, das pessoas ', end='')
for pessoa in dados:
    if pessoa[1] == pesado:
        print(f'[{pessoa[0]}] ', end='')
print()
