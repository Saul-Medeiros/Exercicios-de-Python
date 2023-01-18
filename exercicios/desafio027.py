"""
Desafio 027 - Faça um programa qu eleia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
"""
# deixa todas as palavras da String com a primeira letra em maiúscula:
nome = str(input('Digite seu nome completo: ')).title()
print('Nome informado: {}'.format(nome))
# divide as palavras da variável nome e guarda numa lista:
lista = nome.split()
# informa o primeiro item da lista
print('Primeiro nome: {}'.format(lista[0]))
# len(lista) - 1 insere o tamanho da lista (quantidade de componentes) e
# subtrai 1 para receber a posição do último item dessa lista:
print('Ultimo nome: {}'.format(lista[len(lista) - 1]))
