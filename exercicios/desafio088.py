"""
Desafio 088 - Faça um programa que ajude um jogador da MEGA SENA a criar
palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear
6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep

palpites = []  # lista que irá armazenar as jogadas
print('-' * 33 + f'\n{"JOGOS DA MEGA SENA":^33}\n' + '-' * 33)
n = int(input('Quantos jogos você quer que eu sorteie? '))

# registro de jogos
for jogadas in range(0, n):
    palpites.append(list())  # adiciona uma lista em palpites
    # números da mega sena
    for opcoes in range(0, 6):
        numero = randint(1, 60)  # escolha entre 1 e 60
        if opcoes == 0:
            # armazena o primeiro número randomizado
            palpites[jogadas].append(numero)
        else:
            # evita repetição de números na lista
            while numero in palpites[jogadas]:
                numero = randint(1, 60)
            palpites[jogadas].append(numero)
    # ordena a lista da jogada atual em ordem crescente
    palpites[jogadas].sort()

# impressão dos jogos para o usuário
for jogo, resultado in enumerate(palpites):
    print(f'Jogo {jogo + 1}: {resultado}')
    sleep(1)
print('-=' * 5, '< Boa Sorte! >', '-=' * 5)
