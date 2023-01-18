"""
Desafio 073 - Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na
ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.
"""
brasileirao2018 = 'Palmeiras', 'Flamengo', 'Internacional', 'Grêmio',\
    'São Paulo', 'Atlético MG', 'Atlético PR', 'Cruzeiro', 'BotaFogo',\
    'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará SC',\
    'Vasco da Gama', 'Sport Recife', 'América MG', 'EC Vitória', 'Paraná'
br = '-=' * 15  # barra horizontal
print(br + f'\nBrasileirão Serie A 2018\n' + br +
      '\nLista de times do Brasileirão:', end=' ')
for c in range(0, len(brasileirao2018)):
    print(brasileirao2018[c])
# A)
print(br + '\n5 primeiros colocados: ', end='')
for c in range(0, 5):
    print(brasileirao2018[c], end='')
    if c < 4:
        print(', ', end='')
# B)
print('\n' + br + '\nÚltimos 4 colocados da tabela: ', end='')
for c in range(-1, -5, -1):
    print(brasileirao2018[c], end='')
    if c > -4:
        print(', ', end='')
# C)
print('\n' + br + '\nLista em ordem alfabética: ')
for c in range(0, 20):
    print(sorted(brasileirao2018)[c])
# D)
print(br + '\nPosição da Chapecoense na tabela: '
           f'{brasileirao2018.index("Chapecoense")+1}º lugar')
