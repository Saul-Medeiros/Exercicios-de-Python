"""
Desafio 034 - Escreva um programa que pergunte o salário de um
funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""
print('-=-' * 4, 'AUMENTOS MÚLTIPLOS', '-=-' * 4)
s = float(input('Informe o salário do funcionário: R$'))
# se o salário for maior que R$1250
if s > 1250:
    aum = s * 0.1  # aumento de 10%
    txt = '10%'
# se for menor ou igual a R$1250
else:
    aum = s * 0.15  # aumento de 15%
    txt = '15%'
print('Salário anterior: R${:.2f}'.format(s))
s += aum
print('O funcionário teve um aumento de {} no salário.\n'
      'Valor do aumento: R${:.2f}\n'
      'Novo salário: R${:.2f}'.format(txt, aum, s))
