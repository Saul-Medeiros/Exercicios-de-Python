"""
Desafio 013 - Faça um algoritmo que leia o salário de um funcionário e
mostre seu novo salário, com 15% de aumento.
"""
salario = float(input('Informe o salário do funcionário: R$'))
salario += salario * 0.15
print('''O salário do funcionário teve 15% de aumento.
O salário atual vale R$ {:.2f}'''.format(salario))
