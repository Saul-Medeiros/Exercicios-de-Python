"""
Desafio 036 - Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode
exceder 30% do salário ou então o empréstimo será negado.
"""
from time import sleep
colors = {'boldYellow': '\033[1;33m', 'cyan': '\033[36m',
          'boldWhite': '\033[1;97m', 'boldRed': '\033[1;31m',
          'boldGreen': '\033[1;32m', 'closeColor': '\033[m'}

print(f'{colors["boldWhite"]}-='*5, 'EMPRÉSTIMO BANCÁRIO', '-='*5,
      colors['closeColor'])
priceHouse = float(input('Informe o valor da casa: R$'))
wage = float(input('Informe agora o salário do comprador: R$'))
y = int(input('Informe em quantos anos será quitado o imóvel: '))
months = y * 12  # total de meses para quitação do imóvel
provision = priceHouse / months  # valor da prestação mensal
# tempo para computar os resutlados
print('{}PROCESSANDO...{}'.format(colors['boldYellow'], colors['closeColor']))
sleep(6)
# se a prestação for igual ou menor que 30% do salário
if provision <= (wage * 0.3):
    print('Seu empréstimo para a compra da casa foi '
          f'{colors["boldGreen"]}APROVADO{colors["closeColor"]}!')
    # quantidade de percelas e valor vai aparecer em ciano, o restante d texto
    # vai estar em sua formatação padrao
    print('Valor da prestação: {0}{1}x{3} de {0}R${2:.2f}{3}'
          .format(colors['cyan'], months, provision, colors['closeColor']))
# se a prestação for maior que 30% do salário:
else:
    print(f'Seu empréstimo foi {colors["boldRed"]}NEGADO{colors["closeColor"]},'
          ' pois a prestação da casa\nultrapassa 30% do seu salário.')
