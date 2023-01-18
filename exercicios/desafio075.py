"""
Desafio 075 - Desenvolva um programa que leia quatro valores pelo teclado e
guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'Voce digitou os valores {numeros}')
# A)
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
# B)
print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição' if 3 in numeros
      else 'O valor 3 não foi digitado em nenhuma posição')
# C)
pares = 0
for c in range(0, 4):
    if numeros[c] % 2 == 0:
        pares += 1
if pares > 0:
    print('Os valores pares digitados foram: ', end='')
    for c in numeros:  # c recebe os valores da tupla a cada repetição
        if c % 2 == 0:
            print(c, end=' ')
else:
    print('Não foi informado nenhum número par.')
