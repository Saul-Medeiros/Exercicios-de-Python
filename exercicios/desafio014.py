"""
Desafio 014 - Escreva um programa que converta uma temperatura digitada
em °C e convera para °F.
"""
c = float(input('Informe a temperatura em °C: '))
f = 9 * c / 5 + 32  # Fórmula do Fahrenheit
print('a temperatura de {}°C corresponde a {}°F'.format(c, f))
