"""
Desafio 045 - Crie um programa que faça o computador jogar Jokempô com você.
"""
import emoji
import random
import time
opcoes = ('pedra', 'papel', 'tesoura')  # opções dos jogadores
player = int(input('''Escolha: 
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura: '''))  # escolha do usuário
# escolha inválida:
if player > 2 or player < 0:
    print(emoji.emojize('Escolha inválida :dizzy_face:! Tente novamente '
                        ':slightly_smiling_face:', language='alias'))
    exit()  # finaliza o programa
# randomiza a escolha da cpu
cpuPlay = random.randint(0, 2)
# máquina vai jogar:
print('\n\033[1;36mJO')
time.sleep(1)
print('KEM')
time.sleep(1)
print('PÔ!\033[m\n')
# empate:
if player == cpuPlay:
    print(emoji.emojize('\033[1;97mDeu {} para nós dois '
                        ':monocle_face:!\033[m Vamos denovo :hand_over_mouth:'
                        .format(opcoes[player]), language='alias'))
# resultado;
elif player != cpuPlay:
    # se a cpu ganhar
    if player == 1 and cpuPlay == 2:
        print(emoji.emojize('\033[1;31mEu ganhei :smile:!\033[m Minha tesoura'
                            ' vence seu papel :sunglasses:.', language='alias'))
    elif player == 2 and cpuPlay == 0:
        print(emoji.emojize('\033[1;31mEu ganhei :smile:!\033[m Minha pedra '
                            'vence sua tesoura :sunglasses:.',
                            language='alias'))
    elif player == 0 and cpuPlay == 1:
        print(emoji.emojize('\033[1;31mEu ganhei :smile:!\033[m Meu papel vence'
                            ' a sua pedra :sunglasses:.', language='alias'))
    # se o jogador ganhar:
    else:
        print(emoji.emojize('\033[1;35mVocê ganhou :cry:!\033[m Vamos jogar '
                            'novamente? :nerd_face:', language='alias'))
