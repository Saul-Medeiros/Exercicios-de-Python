"""
Desafio 076 - Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência. No final, mostre uma listagem de
preços, organizando os dados em forma tabular.
"""
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.3,
            'Livro', 34.9)
underline = '-' * 40
print(underline + f'\n{"LISTAGEM DE PREÇOS":^40}\n' + underline)
for c in range(0, len(listagem), 2):  # pula os itens numéricos da listagem
    # String alinhado a esquerda ocupando 30 espaços com pontilhados
    # número alinhado a direita ocupando 6 espaços e mostrando duas casas
    # decimais
    print(f'{listagem[c]:.<30}R${listagem[c+1]:>7.2f}')
print(underline)
