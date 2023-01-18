"""
Desafio 022 - Crie um programa qu e leia o nome completo de uma pessoa
e mostre:
> O nome com todas as letras maiúsculas
> O nome com todas as letras minúsculas
> Quantas letras ao total (sem considerar espaços)
> Quantas letras tem o primeiro nome.
"""
# strip() exclui os espaços indesejados caso haja erro de digitação
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Todas as letras maiúsculas:', nome.upper())
print('Todas as letras minúsculas:', nome.lower())
# total de letras da variável nome - espaços:
print('Quantidade de letras do seu nome completo:',
      (len(nome) - nome.count(' ')))
# total de letras do primeiro item da lista:
print('Quantidade de letras do primeiro nome:', len(nome.split()[0]))
