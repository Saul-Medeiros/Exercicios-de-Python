"""
# Desafio 102 - Crie um programa que tenha uma função fatorial() que receba
dois parâmetros: o primeiro que indique o número a calcular e o outro chamado
show, que será um valor lógico (opcional) indicando se será mostrado ou não na
tela o processo de cálculo do fatorial.
"""


def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado
    :param show: (opcional) Motrar ou não a conta.
    """
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
    print(f'Fatorial do número {num} equivale a {fat}.')
    if show:
        print(f'{num}! = ', end='')
        for c in range(num, 0, -1):
            if c == 1:
                print('1 = ', end='')
                break
            print(f'{c} x ', end='')
        print(f'{fat}')


# main
n = int(input('Informe um númmero para calcular seu fatorial: '))
resp = str(input('Deseja mostrar o processo de cálculo '
                 'do fatorial? [S/N]: ')).strip().upper()[0]
if resp == 'S':
    r = True
elif resp == 'N':
    r = False
else:
    print('Foi informado uma resposta incorreta, portanto, o processo de '
          'cálculo não será mostrado.')
    r = False
fatorial(n, r)
