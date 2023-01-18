"""
Desafio 082 - Crie um programa que vai ler vários números e colocar em uma
lista. Depois disso, crie duas listas extras que vão conter apenas os valores
pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""
lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
for n in range(0, len(lista)):
    pares.append(lista[n]) if lista[n] % 2 == 0 else impares.append(lista[n])
print('-='*30)
print(f'''A lista completa é {lista}
A lista de pares é {pares}
A lista de ímpares é {impares}''')

