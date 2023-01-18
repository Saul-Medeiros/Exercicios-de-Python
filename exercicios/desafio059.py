"""
Desafio 059 - Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
r = 0
while r != 5:
    r = int(input('\nAgora, informe o que deseja fazer'
                  '\n[1] somar'
                  '\n[2] multiplicar'
                  '\n[3] maior'
                  '\n[4] novos números'
                  '\n[5] sair do programa'
                  '\nInforme: '))
    # Caso valor informado não esteja entre as opções do sistema:
    while r > 5 or r < 1:
        r = int(input('Informe uma opção válida e tente novamente: '))
    if r == 1:
        result = n1 + n2
        print(f'A soma de {n1} e {n2} equivale a {result}.')
    elif r == 2:
        result = n1 * n2
        print(f'A multipllicação de {n1} x {n2} equivale a {result}.')
    elif r == 3:
        # predefinição do maior ser o n1 (redução de if)
        result = n1
        # caso n1 não seja o maior, n2 é definido como o novo maior
        if n2 > n1:
            result = n2
        print(f'O maior valor entre {n1} e {n2} é {result}.')
    elif r == 4:
        n1 = float(input('Informe o primeiro número: '))
        n2 = float(input('Informe o segundo número: '))
    else:
        print('Programa finalizado com sucesso.')
    sleep(1.5)
