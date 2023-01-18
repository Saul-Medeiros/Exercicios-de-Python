"""
Desafio 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira e mostre quantos Dólares ela pode comprar.
Considere US$ 1.00 = R$5.22
Euro = EUR€5.55
"""
rs = float(input('Informe o quanto você possui: R$'))
d = rs / 5.22
eur = rs / 5.55
print('Com R${:.2f} você pode comprar US${:.2f} ou €{:.2f}'.format(rs, d, eur))
