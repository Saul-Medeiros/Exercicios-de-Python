"""
Desafio 040 - Crie um programa que leia duas notas de um aluno e
calcule sua média, mostrando uma mensagem no final, de acordo com
a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""
colors = {'red': '\033[31m', 'yellow': '\033[33m',
          'green': '\033[32m', 'close': '\033[m'}
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2) / 2
# end='' concatena o print atual com o próximo
print('Sua média foi {:.2f} e você está '.format(media), end='')
if media >= 7:
    print('{}APROVADO{}'.format(colors['green'], colors['close']))
elif 6.9 >= media >= 5:
    print('de {}RECUPERAÇÃO{}'.format(colors['yellow'], colors['close']))
else:
    print('{}REPROVADO{}'.format(colors['red'], colors['close']))
