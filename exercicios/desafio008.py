"""
Desafio 008 - Escreva um programa que leia um valor em metros e o exiba
convertido em centímetros e milímetros.
"""
m = float(input('Informe uma distância em metros: '))
km = m * 0.001  # quilômetros
hm = m * 0.01  # hectometros
dec = m * 0.1  # decâmetros
dm = m * 10  # decímetros
cm = m * 100  # centímetros
mm = m * 1000  # milímetros
print('''Quilômetros: {}km
Hectômetros: {}hm
Decâmetros: {:.3f}dM
Metros: {}m
Decímetros: {:.0f}dm
Centímetros: {:.0f}cm
Milímetros: {:.0f}mm'''.format(km, hm, dec, m, dm, cm, mm))
# {:.0f} aplica a formatação e 0 números aparecerem depois da vírgula para as
# variáveis.
