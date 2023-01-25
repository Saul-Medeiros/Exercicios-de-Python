from desafio115.lib.interface import *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')  # reading text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        # escrever um novo arquivo de texto
        a = open(nome, 'wt+')  # write text+
        a.close()
    # caso dê um erro generalizado
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for line in a:
            # remove o ; e usa como referência para dividir as strings
            dado = line.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')  # append text
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
