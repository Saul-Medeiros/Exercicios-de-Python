"""
Desafio 029 - Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi
multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""
print('-=-' * 3, 'RADAR ELETRÔNICO', '-=-' * 3)
v = int(input('Qual é a velocidade atual do seu carro? '))
if v > 80:
    multa = 7 * (v - 80)  # multa aplicada por km ultrapassado
    print('Você ultrapassou o limite máximo e foi multado!'
          '\nValor da multa: R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')
