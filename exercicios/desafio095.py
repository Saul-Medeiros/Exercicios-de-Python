"""
Desafio 095 - Aprimore o desafio 093 para que ele funcione com vários
jogadores, incluindo um sistema de visualização de detalhes do aproveitamento
de cada jogador.
"""
# lista que armazenará os jogadores
jogadores = list()
# dicionário que irá armazenar o jogador
jogador = dict()
# lista interna que armazenará a quantidade de gols em cada partida do
# jogador atual:
gols = list()

# cadastro de jogadores
while True:
    # limpa o dicionário para o próximo jogador
    jogador.clear()
    # limpa a lista de gols para declaração do próximo jogador
    gols.clear()
    print('-' * 30)
    jogador['nome'] = str(input('Nome do Jogador: ')).title().strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    # cadastro de gols por partida
    for partida in range(0, partidas):
        gols.append(int(input(f'Quantos gols na {partida + 1}ª partida? ')))
    # armazena uma cópia da lista de gols do jogador no dicionáro do mesmo
    jogador['gols'] = gols[:]
    # soma todos os itens registrados na lista
    jogador['total'] = sum(gols)
    # armazena uma cópia do dicionário do jogador atual na lista de jogadores
    jogadores.append(jogador.copy())
    # verifica respostas incorretas a cada repetição
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            # finaliza a repetição interna
            break
        print('Resposta inválida. Tente novamente.')
    if resp == 'N':
        # finaliza a repetição externa
        break
print('-=' * 30)

# resultado geral
print('cod ', end='')
# para cada key (nome, gols, total) no dicionário do jogador
for i in jogador.keys():
    # keys ocupa 15 espaços alinhado a esquerda
    print(f'{i:<15}', end='')
print('\n' + '-' * 40)
# k = posição do jogador na lista | v = dicionário do jogador
for k, v in enumerate(jogadores):
    # posição ocupa 3 casas, alinhado a direita
    print(f'{k:>3} ', end='')
    # para cada value (correspondente a nome, gols e total) no dicionário do
    # jogador correspondente
    for d in v.values():
        # values convertido para String, ocupa 15 espaços alinhado a esquerda
        print(f'{str(d):<15}', end='')
    print()

# resultado por jogador
while True:
    print('-' * 40)
    consulta = int(input('Mostrar dados de qual jogador? [999 interrompe]: '))
    # valor informado está entre disponíveis para consulta
    if consulta < len(jogadores):
        # aproveitamento do jogador (redefinido a cada repetição externa)
        aprov = 0
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[consulta]["nome"]}:')
        # j: para cada partida, p: recebe o número de gols
        for v, p in enumerate(jogadores[consulta]['gols']):
            print(f'    No jogo {v + 1} fez {p}')
            # se na partida atual o jogador tiver feito gols
            if p > 0:
                aprov += 1
        # porcentagem de aproveitamento do jogador correspondente
        aprov *= 100 / len(jogadores[consulta]['gols'])
        print(f'Aproveitamento de {aprov:.2f}% dos jogos.')
    # se consulta for diferente de 999
    elif consulta != 999:
        print(f'ERRO! Não existe jogador com código {consulta}!'
              ' Tente novamente')
    # se consulta equivaler a 999
    else:
        break
print('<< VOLTE SEMPRE >>')
