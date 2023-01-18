"""
Desafio 002 - Crie um script Python que leia o dia, o mês e o ano de nascimento
de uma pessoa e mostre uma mensagem com a data formatada.
"""
dia = input('Dia = ')
mes = input('Mês = ')
ano = input('Ano = ')
# informações de texto mescladas com número, por isso o uso de vírgula e
# concatenação:
print('Você nasceu no dia', dia, 'de ' + mes + ' de', ano, '. Correto?')
