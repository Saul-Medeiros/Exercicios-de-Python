"""
Desafio 071 - Crie um programa que simule o funcionamento de um caixa
eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado
(número inteiro) e o proggrama vai informar quais cédulas de cada valor serão
entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
"""
print('='*32 + f'\n{"NUBANK":^32}\n' + '='*32)
# variável valor permanece constante enquanto a variável restante é modificada
valor = restante = int(input('Que valor você quer sacar? R$'))
cont = 0  # contador auxiliar para a variável cedulas
# fatiamento do valor
while True:
    #          0   1   2   3
    cedulas = [50, 20, 10, 1]
    if restante >= cedulas[cont]:
        print(f'Total de {restante // cedulas[cont]} cédulas '
              f'de R${cedulas[cont]}')
        restante %= cedulas[cont]
    cont += 1
    if cont == 4:
        break
print('='*32 + '\nTenha um excelente dia!')
