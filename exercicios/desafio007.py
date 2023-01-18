"""
Desafio 007 - Desenvolva um programa que leia as duas notas de um aluno,
calcule e mostre a sua média.
"""
nome = input('Informe o nome do aluno: ')
n1 = float(input('Informe a primeira nota do aluno: '))
n2 = float(input('Informe a segunda nota do aluno: '))
media = (n1 + n2) / 2
print('O aluno {} ficou com uma média de {:.2f} no bimestre.'
      .format(nome, media))
# Resultado: O aluno <nome> ficou com uma média de <media> no bimestre.
# Implementa a formatação de até duas casas após a vírgula na média.
