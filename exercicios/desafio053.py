"""
Desafio 053 - Crie um programa que leia uma frase qualquer e diga se
ela é um palindromo, desconsiderando os espaços. (Ler de trás pra
frente sem alterar o sentido da frase)
Ex:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
"""
# remove espaços indesejados, deixa todos os caracteres em maiúsculo,
# divide a frase:
frase = str(input('Digite uma frase para verificação: ')).strip().upper().\
    split()
# une a frase sem os espaços:
frase = ''.join(frase)
# variável para armazenar a frase ao contrário desconsiderando os espaços:
inverso = ''
for letra in range(len(frase) - 1, -1, -1):
    inverso += frase[letra]
# Dessa forma não precisaria da estrutura de repetição e o programa
# iria funcionar normalmente:
# inverso = frase[::-1]
print(f'A frase {frase} possui o seu inverso {inverso},\nportanto, ela', end='')
if inverso == frase:
    print(' é um palíndromo.')
else:
    print(' não é um palíndromo.')
