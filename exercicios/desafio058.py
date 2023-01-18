"""
Desafio 058 - Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em
um número entre 0 e 10. Só que agora o jogador vai tentar advinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""
from time import sleep
from random import randint
cores = {'azul': '\033[34m', 'vermelho': '\033[31m',
         'verde': '\033[32m', 'exit': '\033[m'}
print('Vou pensar em um número entre 0 e 10. Tente advinhar', end='')
for c in range(0, 3):
    print(end='.')
    sleep(1)
n = int(input('\nEm que número eu pensei? '))  # Advinhação do jogador
# Caso seja informado um valor incorreto:
while n > 10 or n < 0:
    n = int(input('Número inválido! Informe um número entre 0 e 10: '))
cpu = randint(0, 10)  # Valor pensado pelo computador
cont = 1
while n != cpu:
    print('{}PROCESSANDO'.format(cores['azul']), end='')
    # Gerador de ponto final para a frase anterior:
    for c in range(0, 3):
        print(end='.')
        sleep(1)  # 1 segundo de delay
    print('{0}\nVocê {1}ERROU{0} o seu palpite, tente novamente. '
          .format(cores['exit'], cores['vermelho']))
    # Informa se o valor informado foi maior ou menor que o computador "pensou"
    if n > cpu:
        n = int(input('Dica: é um número menor do que você digitou.\n'
                      'Informe: '))
    elif n < cpu:
        n = int(input('Dica: é um número maior do que você digitou.\n'
                      'Informe: '))
    cont += 1  # O contador só vai contar as tentativas com números válidos
    # Verificador de valor:
    while n > 10 or n < 0:
        n = int(input('Número inválido! Informe um número entre 0 e 10: '))
# Repetição do processamento para impressão do resultado caso esteje certo:
print('{}PROCESSANDO'.format(cores['azul']), end='')
# Gerador de ponto final para a frase anterior:
for c in range(0, 3):
    print(end='.')
    sleep(1)  # 1 segundo de delay
print('{0}\nVocê {1}ACERTOU{0}! Mas foram necessários {2} tentativas para '
      'você advinhar.'.format(cores['exit'], cores['verde'], cont))
