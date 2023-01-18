"""
Desafio 024 - Crie um program aque leia o nome de um a cidade e diga
se ela começa ou não com o nome "SANTO".
"""
cid = str(input('Em que cidade você nasceu? ')).strip()
# retorna False ou True de acordo com a primeira palavra da cidade informada:
print('SANTO' in cid.upper().split()[0])
# upper() deixa todas as letras maiúsculas
# split() separa as palavras em lista
# [0] pega o primeiro item da lista
