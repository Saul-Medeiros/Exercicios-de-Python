"""
Desafio 101 - Crie um programa que tenha uma função chamada voto() que vai
receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor
literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas
eleições.
"""
from datetime import date


def voto(ano):
    """
    Indica a situação eleitoral do usuário de acordo com a sua idade.
    :param ano: Recebe o ano de nascimento do usuário.
    :return: Situação do eleitor
    """
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return 'foi NEGADO'
    elif 18 > idade >= 16 or idade >= 65:
        return 'é OPCIONAL'
    else:
        return 'é OBRIGATÓRIO'


def titulo():
    print('-=' * 11)
    print('  Situação Eleitoral')
    print('-=' * 11)


# Programa principal
titulo()
nasc = int(input('Informe o ano em que nasceu: '))
print(f'O seu voto nas eleições {voto(nasc)}.')
