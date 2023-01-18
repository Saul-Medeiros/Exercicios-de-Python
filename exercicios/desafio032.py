"""
Desafio 032 - Faça um programa que leia um ano qualquer e mostre se
ele é BISSEXTO.
"""
from datetime import date
print('-=-' * 4, 'ANO BISSEXTO', '-=-' * 4)
y = int(input('Informe o ano que deseja analisar\n'
              '(digite 0 caso queira analisar o ano atual): '))
if y == 0:
    # data.hoje().ano
    # classe.método().atributo
    y = date.today().year
"""
Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando com 
366 dias, um dia a mais do que os anosnormais de 365 dias, ocorrendo a cada 
quatro anos (exceto anos múltiplos de 100 que não são múltiplos de 400).
"""
# se ano for múltiplo de 4 e múltiplo de 400
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print('O ano {} tem 366 dias, portanto é um ano bissexto!'.format(y))
# se ano não for múltiplo de 4, for múltiplo de 100 mas não for múltiplo de 400
else:
    print('O ano {} tem 365 dias, então não é um ano bissexto.'.format(y))
