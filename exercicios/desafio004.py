"""
Desafio 004 - Faça um programa que leia algo pelo teclado e mostre na tela o
seu tipo primitivo e todas as informações possíveis sobre ele.
"""
x = input('Digite algo: ')
print('Tipo de variável: ', type(x))
print('É alfanumérico? ', x.isalnum())
print('É alfabético? ', x.isalpha())
print('É um número? ', x.isnumeric())  # mesma coisa que isdigit
print('Faz parte da tabela ascii? ', x.isascii())
print('É dígito? ', x.isdigit())
print('Tem todas as letras em maiúsculo? ', x.isupper())
print('Tem todas as letras minúsculas? ', x.islower())
print('É um número entre entre 0 e 9? ', x.isdecimal())
"""
O método isidentifier() retorna True se a string for um identificador válido, 
caso contrário, False. Uma string é considerada um identificador válido se 
tiver apenas letras alfanuméricas (a-z) e (0-9) ou sublinhados (_).
Um identificador válido não pode começar com um número ou conter espaços.
"""
print('É um texto válido para o Python? ', x.isidentifier())
"""
O método isprintable() retorna “True” se todos os caracteres na string são 
imprimíveis ou a string está vazia, caso contrário, retorna “False”. Esta 
função é usada para verificar se o argumento contém algum caractere imprimível.
"""
print('É printável? ', x.isprintable())
# também é possivel usar formatação em chamada de métodos
print('Só tem espaços? {}'.format(x.isspace()))
"""
O método istitle() verifica se as primeiras letras de cada palavra são 
maiúsculas e se for apenas letras retorna True
"""
print('Está capitalizada? {}'.format(x.istitle()))
