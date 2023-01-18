"""
Desafio 077 - Crie um programa que tenha uma tupla com várias palavras (não
usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as
suas vogais.
"""
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:  # p recebe uma palavra da tupla a cada repetição
    print(f'Na palavra {p.upper()} temos ', end='')
    for letra in p:  # toda String é uma tupla, composta por n caracteres
        if letra in 'aeiou':  # se o caractere atual está entre as vogais
            print(letra, end=' ')  # impressão da vogal
    print()  # pula linha
