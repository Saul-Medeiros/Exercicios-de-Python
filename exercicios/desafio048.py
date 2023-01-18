"""
Desafio 048 - Faça um programa que calcule a soma entre todos os
números ímpares que são múltiplos de 3 e que se encontrem no
intervalo de 1 até 500.
"""
soma = 0
for c in range(1, 501, 2):
    # Se número é múltiplo de 3
    if c % 3 == 0:
        soma += c
print(f'A soma entre todos os números ímpares que são múltiplos de 3 é {soma}.')
