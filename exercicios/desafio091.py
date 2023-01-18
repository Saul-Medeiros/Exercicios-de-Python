"""
Desafio 091 - Crie um programa onde 4 jogadores joguem um dado e tenham
resultados aleatórios. Guarde esses resultados em um dicionário. No final,
coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número
no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter

jogos = dict()  # dicionário de jogadores

# preenche o dicionário com os respectivos jogadores e suas jogadas
for jogo in range(1, 5):
    jogos[f'Jogador {jogo}'] = randint(1, 6)

# resultado
print(f'{"<<< VALORES SORTEADOS >>>":^28}')
# para keys e values em cada item de jogo
for k, v in jogos.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
print()

# colocação
print('<<< RANKING DOS JOGADORES >>>')
# ordena o dicionário dentro de uma lista, em ordem decrescente, baseado
# nos valores(values) de cada item, separando cada item por tuplas
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
# [(key, value), (key, value), (key,value), (key, value)]
#              maior value → menor value

# para cada posição na lista, jogador recebe key (Jogador ...)
for pos, jogador in enumerate(ranking):
    print(f' {pos + 1}º lugar: {jogador[0]} tirou {jogador[1]}')
