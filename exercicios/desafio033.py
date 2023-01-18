"""
Desafio 033 - Faça um programa que leia três números e mostre qual
é o maior e qual é o menor.
"""
print('-=-' * 4, 'MAIOR E MENOR VALORES', '-=-' * 4)
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('terceiro valor: '))
maior = menor = n1
if n2 > n3 and n2 > n1:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
elif n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
print(f'''Entre os valores informados, {maior} é o maior valor e 
{menor} é o menor valor.''')
