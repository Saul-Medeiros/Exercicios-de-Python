"""
Desafio 041 - A Confederação Nacional de Natação precisa de um
programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
"""
from datetime import date

birthY = int(input('Informe o ano de nascimento do atleta: '))
# ano atual:
currentY = date.today().year

# cores:
colors = {'cyan': '\033[1;36m', 'yellow': '\033[1;33m',
          'red': '\033[1;31m', 'magenta': '\033[1;35m',
          'b&w': '\033[1;30;107m', 'close': '\033[m'}
if birthY < currentY:
    print('Atleta', end=' ')
    if currentY - birthY <= 9:
        print(colors['cyan'] + 'MIRIM' + colors['close'])
    elif currentY - birthY <= 14:
        print(colors['yellow'] + 'INFANTIL' + colors['close'])
    elif currentY - birthY <= 19:
        print(colors['red'] + 'JÚNIOR' + colors['close'])
    elif currentY - birthY <= 25:
        print(colors['magenta'] + 'SÊNIOR' + colors['close'])
    else:
        print(colors['b&w'] + 'MASTER' + colors['close'])
else:
    print('Idade inválida, tente novamente.')
