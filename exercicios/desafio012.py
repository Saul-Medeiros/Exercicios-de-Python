"""
Desafio 012 - Faça um algoritmo que leia o preço de um produto e mostre seu
novo preço, com 5% de desconto.
"""
price = float(input('Informe o preço do produto: R$'))
newPrice = price - (price * 0.05)  # calcula desconto
print('O produto que custava R${:.2f}, com desconto de 5% passará '
      'a custar R${:.2f}'.format(price, newPrice))
