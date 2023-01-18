"""
Desafio 028 - Escreva um programa que faça o computador "pensar" em
um número entre 0 e 5 e peça para o usuário tentar descobrir qual foi
o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
# randomização de números inteiros
from random import randint
# faz o computador ter um delay antes de mostrar as próximas informações
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
n = int(input('Em que número eu pensei? '))  # Advinhação do jogador
# Se o número digitado for inválido:
while n > 5 or n < 0:
    n = int(input('Número inválido! Informe um número entre 0 e 5: '))
# "Pensamento" randomizado do computador:
cpu = randint(0, 5)
print('PROCESSANDO...')
# Tempo em segundos para o delay de informações mostradas pelo computador:
sleep(5)  # 5 segundos
print(f'GANHEI! Eu pensei no número {cpu} e não no {n}!' if n != cpu else
      f'VOCÊ GANHOU! Você pensou no número {n} assim como eu, PARABÉNS!')
