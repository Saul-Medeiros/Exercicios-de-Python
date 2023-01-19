"""
Desafio 103 - Faça um programa que tenha uma função chamada ficha(), que receba
dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado
não tenha sido informado corretamente.
"""


def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


n = str(input('Nome do Jogador: ')).strip().title()
g = str(input('Número de Gols: '))
# se g for numérico
if g.isnumeric():
    # transforma str em int
    g = int(g)
else:
    g = 0
# se jogador não tiver texto
if n == '':
    ficha(gols=g)
else:
    ficha(n, g)
