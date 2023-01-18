"""
Desafio 011 - Faça um programa que leia a largura e a altura de uma parede em
metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2m².
"""
h = float(input('Informe a altura da parede: '))  # height
w = float(input('Informe a largura da parede: '))  # width
a = h * w  # area
qt = a / 2
print('Área da parede: {}m²\nQuantidade de tinta necessária '
      'para a pintura: {}l.'.format(a, qt))
