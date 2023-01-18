"""
Desafio 039 - Faça um programa que leia o ano de nascimento de um
jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou
do prazo.
"""
import emoji
from datetime import date
currentY = date.today().year
birthY = int(input('Informe o ano de seu nascimento: '))
sexo = int(input('''Informe seu sexo:
[ 1 ] - Masculino
[ 2 ] - Feminino
Informe: '''))
if birthY < currentY:
    # calcula a idade atual da pessoa:
    age = currentY - birthY
    if sexo == 1:
        if age < 18:
            # calcula quantos anos faltam para o alistamento referente
            # ao ano atual:
            missing = 18 - age
            print(f'Faltam {missing} ano(s) para o seu alistamento '
                  'obrigatório.')
        elif age > 18:
            print(f'Se passaram {age - 18} anos do seu alistamento '
                  'obrigatório.')
        else:
            # emoji: 🚨
            print(emoji.emojize(':rotating_light: É hora de se alistar! '
                                ':rotating_light:', language='alias'))
    elif sexo == 2:
        print(f'Você tem  atualmente {age} anos e seu alistamento miltar '
              'é opcional.')
    else:
        print('Informe um sexo válido e tente novamente.')
else:
    print('Ano de nascimento inválido, tente novamente.')
