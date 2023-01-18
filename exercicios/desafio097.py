"""
Desafio 097 - Faça um programa que tenha uma função chamada escreva(), que
receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho
adaptável.
Ex:
escreva('Olá, Mundo!')

Saída:
---------------
  Olá, Mundo!
---------------
"""


# Função
def escreva(txt):
    tam = len(txt) + 4
    print('-' * tam)
    print(f'  {txt}')
    print('-' * tam)


# Programa Principal
escreva(str(input('Escreva um texto para ser adaptado: ').strip()))
