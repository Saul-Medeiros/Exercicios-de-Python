"""
Desafio 070 - Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá peguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais barato
"""
barato = ''
vt = highprice = lowprice = cont = 0
print('\033[1m-'*41 + f'\n{"AMAZON BRASIL":^41}\n' + '-'*41 + '\033[m')
while True:
    produto = str(input('Nome do Produto: ')).strip().title()
    preco = float(input('Preço: R$'))
    vt += preco  # soma o total de gastos
    cont += 1  # contador auxiliar
    if cont > 1:
        if preco < lowprice:
            barato = produto
            lowprice = preco
    # o primeiro produto vai ser usado como comparação aos demais
    else:
        barato = produto
        lowprice = preco
    if preco > 1000:
        highprice += 1
    resp = ' '  # redefine a resposta quando recomeça o loop
    while resp not in 'SN':
        resp = str(input('Quer continuar? [s/n]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'''{" FIM DO PROGRAMA ":-^41}
Total da compra: R${vt:.2f}
Temos {highprice} produtos custando mais de R$ 1000.00
O produto mais barato foi {barato} que custa R${lowprice:.2f}''')
