"""
Desafio 037 - Escreva um programa que leia um número inteiro
qualquer e peça para o usuário escolher qual será a base de
conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""
colors = {'boldWhite': '\033[1;97m', 'red': '\033[31m',
          'yellow': '\033[33m', 'blue': '\033[34m',
          'close': '\033[m'}
print(f'{colors["boldWhite"]}=-'*5, 'CONVERSOR DE NÚMERO',
      '-='*5, colors['close'])
n = int(input('Informe um valor: '))
bc = int(input('''Informe agora qual será a base de conversão
{0}[ 1 ]{1} para {0}binário{1}, 
{2}[ 2 ]{1} para {2}octal{1} ou 
{3}[ 3 ]{1} para {3}hexadecimal{1}: '''.format(colors['red'], colors['close'],
                                   colors['yellow'], colors['blue'])))
# informado um número entre 1 e 3:
if bc == 1:
    txt = 'binária'
    print(f'{n} em base binária: {colors["red"]}{bin(n)[2:]}{colors["close"]}')
elif bc == 2:
    print(f'{n} em base octal: {colors["yellow"]}{oct(n)[2:]}{colors["close"]}')
elif bc == 3:
    print(f'{n} em base hexadecimal: '
          f'{colors["blue"]}{hex(n)[2:]}{colors["close"]}')
# informado um número inválido:
else:
    print('Você não informou um número válido, tente novamente.')
