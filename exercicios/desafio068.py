"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será
interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
"""
from random import randint
from time import sleep
v = 0  # contador de vitórias
jogador = ' '  # escolha do jogador (nulo pré definido)
print('\033[1m-='*26 + '\nVamos Jogar PAR ou ÍMPAR\n' + '-='*26)
while True:
    num = int(input('Diga um valor: '))
    cpu = randint(0, 10)
    # enquanto jogador não estiver na string PI (inicialmente não vai estar
    # para poder entrar no loop)
    while jogador not in 'PI':
        jogador = str(input('PAR ou ÍMPAR? [P/I]: ')).strip().upper()[0]
    # recebe par ou ímpar de acordo com a escolha
    jogador = 'PAR'
    if jogador == 'I':
        jogador = 'ÍMPAR'
    soma = num + cpu
    # recebe a respectiva designação e acordo com a soma dos valores:
    resultado = 'PAR' if soma % 2 == 0 else 'ÍMPAR'
    print('-'*52 + f'\nVocê jogou {num} e o computador {cpu}. Total de '
                   f'{soma} deu {resultado}.')
    print('-'*52)
    if jogador != resultado:
        print('Você PERDEU!\n' + '-='*26)
        break  # game over
    print('Você VENCEU!\nVamos jogar novamente...\n' + '-='*26)
    v += 1
    sleep(2)  # 2 segundos
print('-=' * 26 + f'\nGAME OVER! Você venceu {v} vezes.\033[m')
