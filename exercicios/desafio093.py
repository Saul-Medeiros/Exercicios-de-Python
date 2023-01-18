"""
Desafio 093 - Crie um programa que gerencie o aproveitamento de um jogador de
futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo
isso será guardado em um dicionário, inclundo o total de gols feitos durantte
o campeonato.
"""
# informações do jogador
jogador = dict()
# quantidade de partidas e gols
gols = list()

# registro
jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for partida in range(0, partidas):
    gols.append(int(input(f'Quantos gols na {partida + 1}ª partida? ')))
jogador['gols'] = gols[:]  # recebe uma cópia da lista 'gols'
jogador['total'] = sum(gols)  # recebe a soma de todos os itens da lista 'gols'
print('-=' * 30)

# resultado 1
print(jogador)
print('-=' * 30)

# resultado 2
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)

# resultado 3
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
# índice da lista | valor do gol
for i, v in enumerate(jogador['gols']):
    print(f'    => Na {i + 1}ª partida, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
