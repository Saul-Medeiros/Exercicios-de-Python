"""
Desafio 051 - Desenvolva um programa que leia o primeiro termo e a
razão de uma Progressão Aritmética. No final, mostre os 10 primeiros
termos dessa progressão.
"""
termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
decimo = termo + (10 - 1) * razao  # fórmula para o enésimo termo da PA
n = 1
for c in range(termo, decimo + razao, razao):
    print(f'{n}° termo: {c}')
    n += 1
