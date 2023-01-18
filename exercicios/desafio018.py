"""
Desafio 018 - Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse ângulo.
"""
# importação das funções seno, cosseno e tangente e conversor para radiano
from math import sin, cos, tan, radians
ang = int(input('Informe um ângulo: '))
sen = sin(radians(ang))  # retorna o seno do número informado
cos = cos(radians(ang))  # retorna o cosseno do número informado
tan = tan(radians(ang))  # retorna a tangente do número informado
# radians formata o número para grau radiano
print('O ângulo de {}° possui o seno no valor de {:.2f},'
      '\no cosseno no valor de {:.2f}'
      '\ne a tangente no valor de {:.2f}'.format(ang, sen, cos, tan))
