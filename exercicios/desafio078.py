"""
Desafio 078 - faça um programa que leia 5 valores numéricos e guarde-os em uma
lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
posições na lista.
"""
lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor na posição {cont}: ')))
print(f'Valores informados: {lista}')
print(f'O maior valor foi {max(lista)}, encontrado nas posições ', end='')
for maior in range(0, len(lista)):
    if max(lista) == lista[maior]:
        print(f'{maior}... ', end='')
print(f'\nO menor valor foi {min(lista)}, encontrado nas posições ', end='')
for menor in range(0, len(lista)):
    if min(lista) == lista[menor]:
        print(f'{menor}... ', end='')
print()
