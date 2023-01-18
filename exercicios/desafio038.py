"""
Desafio 038 - Escreva um programa que leia dois números inteiros e
compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""
colors = {'whitebold': '\033[1;97m', 'magenta': '\033[35m',
          'blue': '\033[34m', 'close': '\033[m'}
print(colors['whitebold'] + '=-'*5,
      'COMPARAÇÃO DE NÚMEROS', '-='*5, colors['close'])
n1 = int(input(colors['magenta'] + 'Informe um número: ' + colors['close']))
n2 = int(input(colors['blue'] + 'Informe outro número: ' + colors['close']))
if n1 > n2:
    print(f'{colors["magenta"]}O primeiro valor é maior.{colors["close"]}')
elif n1 < n2:
    print(f'{colors["blue"]}O segundo valor é maior.{colors["close"]}')
else:
    print('Não existe valor maior, os dois são iguais.')
