"""
Desafio 035 - Desenvolva um programa que leia o comprimento de três
retas e diga ao usuário se elas podem ou não formar um triângulo.
"""
print('-=' * 20 + '\nANALISADOR DE TRIÂNGULOS\n' + '-=' * 20)
a = float(input('Informe a medida da primeira reta: '))
b = float(input('Agora, informe a medida da segunda reta: '))
c = float(input('Por último, informe a medida da terceira reta: '))
# todos os lados tem que ser menor que a soma dos outros dois para
# formar um triângulo
if a < (b + c) and b < (a + c) and c < (a + b):
    # Todos os lados iguais:
    if a == b == c:
        tipo = 'Equilátero'
    # Todos os lados diferentes:
    elif a != b != c:
        tipo = 'Escaleno'
    # Um lado diferente dos outros dois:
    else:
        tipo = 'Isósceles'
    print('As três retas informadas formam um triângulo {}'.format(tipo))
else:
    print('As retas informadas não formam um triângulo.')
