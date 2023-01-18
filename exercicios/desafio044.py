"""
Desafio 044 - Elabore um programa que calcule o valor a ser pago por
um produto, considerando o seu preço normal e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

produto = float(input('Informe o valor das compras: R$'))
condicao = int(input('''Informe a sua condição de pagamento:
1 - à vista no cheque/dinheiro
2 - à vista no cartão
3 - em até 2x no cartão
4 - 3x ou mais no cartão
Informe: '''))
print()  # pula 1 linha
if condicao == 1:
    print('Você tem 10% de desconto para pagamentos a vista e\n'
          'vai pagar apenas R${:.2f}'.format(produto - (produto * 0.1)))
elif condicao == 2:
    print('Você tem 5% de descontto para pagamentos a vista no cartão e\n'
          'vai pagar apenas R${:.2f}'.format(produto - (produto * 0.05)))
elif condicao == 3:
    print('''Você pagará o preço normal do produto: R${:.2f}
    Parcelado em 2x de: R${:.2f}'''.format(produto, produto / 2))
elif condicao == 4:
    parcela = int(input('Em quantas vezes vai querer parcelar? '))
    juros = produto + (produto * 0.2)
    print(f'Você terá juros de 20% por ter parcelado em {parcela}x no cartão.'
          f'\nValor total a pagar: R${juros:.2f}'
          f'\nValor da parcela: R${juros / parcela:.2f}')
else:
    print('Informe uma condição válida e tente novamente.')
