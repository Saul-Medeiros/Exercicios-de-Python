"""
Desafio 085 - Crie um programa onde o usuário possa digitar sete valores
numéricos e cadastre-os em uma lista única que mantenha separados os valores
pares e ímpares. No final, mostre os valores pares e ímpares em ordem
crescente.
"""
# valor, par, ímpar
numeros = [[], [], []]
for cont in range(0, 7):
    numeros[0].append(int(input(f'Digite o {cont + 1} valor: ')))
    if numeros[0][cont] % 2 == 0:
        # adiciona o valor na listagem de pares
        numeros[1].append(numeros[0][cont])
    else:
        # adiciona o valor na listagem de ímpares
        numeros[2].append(numeros[0][cont])
# ordena as listas internas em ordem crescente
numeros[1].sort()
numeros[2].sort()
print(f'''\nValores digitados: {numeros[0]}
Valores pares digitados: {numeros[1]}
Valores ímpares digitados: {numeros[2]}''')
