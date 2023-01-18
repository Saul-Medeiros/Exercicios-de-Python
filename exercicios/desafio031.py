"""
Desafio 031 - Desenvolva um programa que pergunte a distância de uma
viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km
para viagens de até 200Km e R$0,45 para viagens mais longas.
"""
print('-=-' * 4, 'CUSTO DA VIAGEM', '-=-' * 4)
d = float(input('Informe a distância da viagem em Km: '))
# se a distância tiver valor acima de 0:
if d > 0:
    # se a viagem for até 200Km
    if d <= 200:
        price = 0.5 * d  # 50 centavos por Km percorrido
        print('Você percorrerá {:.0f}km e terá que pagar R${:.2f} '
              'de passagem.'.format(d, price))
    # se a viagem for mais longa
    else:
        price = 0.45 * d  # 45 cntavos por Km percorrido
        print('Você percorrerá {:.0f}km e terá que pagar R${:.2f} '
              'de passagem.'.format(d, price))

    """
    # Outra forma de fazer:
    price = d * 0.5 if d <= 200 else d * 0.45  # condição simplificada
    """

# se distância tiver valor nulo ou negativo:
else:
    print('Distância inválida! Tente novamente.')
