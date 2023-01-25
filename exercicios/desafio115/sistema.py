"""
Desafio 115 - Crie um pequeno sistema modularizado que permita cadastrar
pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as
pessoas cadastradas.
"""
from desafio115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa',
                     'Sair do Sistema'])
    if resposta == 1:
        # opção de listar o conteúdo de um arquivo
        lerarquivo(arq)
    elif resposta == 2:
        # opção de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        # digitou uma opção errada no menu
        print(f'{cores(1)}ERRO! Digite uma opção válida!{cores()}')
    sleep(2)
