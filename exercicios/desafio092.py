"""
Desafio 092 - Crie um programa que leia nome, ano de nascimento e carteira de
trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for
diferente de ZERO, o dicionário receberá também o ano de contratação e o
salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai
se aposentar. Considere 35 anos de contribuição a partir da data da carteira
assinada.
"""
from datetime import date

atual = date.today().year
oitentaanos = date.today().year - 80  # limite máximo de idade para registro
dados = dict()

dados['nome'] = str(input('Nome: ')).strip().title()
nasc = int(input('Ano de Nascimento: '))

# verifica idade informada incorretamente (se maior de 80 ou nascimento
# pós ano atual):
while nasc >= atual or nasc < oitentaanos:
    nasc = int(input('Ano de nascimento inválido, tente novamente: '))
dados['idade'] = atual - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

# verificação de ctps e idade permitida para clt
if dados['ctps'] != 0 and dados['idade'] >= 16:
    dados['contratação'] = 0  # recebe valor nulo para verificação
    while dados['contratação'] - 16 < nasc:
        dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    # idade de aposentadoria:
    dados['aposentadoria'] = dados['contratação'] + 35 - nasc
print()

# exibição de registro do civil
print('-' * 30 + f'\n{"Registro Civil":^30}\n' + '-' * 30)
print(f'''NOME: {dados["nome"]}
IDADE: {dados["idade"]}
CTPS: {dados["ctps"]}''', end='\n')
if dados['ctps'] != 0:
    print(f'ANO DE CONTRATAÇÃO: {dados["contratação"]}'
          f'\nSALÁRIO: R${dados["salário"]:.2f}'
          f'\nAPOSENTADORIA: {dados["aposentadoria"]}')
print('-' * 30)
