"""
Desafio 006 - Crie um algoritmo que leia um número e mostre o seu dobro,
triplo e raiz quadrada.
"""
n1 = int(input('Informe um número: '))
dobro = n1 * 2
triplo = n1 * 3
raizq = n1 ** (1/2)  # Outra forma de fazer: pow(n, (1/2))
"""
O {} também pode reconhecer as posições de cada variável utilizada no format 
similar a um vetor, iniciando em 0
{3:.2f} utiliza o número que está na 3ª posição (no caso o 4º número) e formata 
com 2 dígitos após a vírgula
"""
print('O dobro do número {0} é {1}, o triplo de {0} é {2} e a'
      '\nraiz quadrada de {0} é {3:.2f}.'.format(n1, dobro, triplo, raizq))
# Resultado: O dobro do número <n1> é <dobro>, o triplo de <n1> é <triplo> e a
# raiz quadrada de <n1> é <raizq>.
