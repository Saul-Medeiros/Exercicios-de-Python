"""
Desafio 096 - Faça um programa que tenha uma função chamada área(), que receba
as dimensões de um terreno retangular (largura e comprimento) e mostre a área
do terreno.
"""


def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno {larg}x{comp} equivale a {a}m².')


# Programa principal
print(' Controle de Terrenos')
print('-' * 22)
medidas = (
    float(input('Largura (m): ')),
    float(input('Comprimento (m): '))
)
area(medidas[0], medidas[1])
