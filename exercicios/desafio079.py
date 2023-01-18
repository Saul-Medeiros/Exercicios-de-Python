"""
Desafio 079 - Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já esteja lá dentro, ele
não será adicionando. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente.
"""
lista = []
cont = 1
while True:
    num = int(input(f'Informe o {cont}º valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
    cont += 1
lista.sort()  # ordena lista em crescente (alteração)
print(f'Lista de valores informados: {lista}')
