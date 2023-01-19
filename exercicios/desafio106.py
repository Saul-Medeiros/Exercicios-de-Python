"""
Desafio 106 - Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário
digitar a palavra 'FIM', o programa se encerrará.
OBS: use cores.
"""


def title():
    """
    Título do Sistema de Ajuda PyHELP.
    """
    # style = bold, textcolor = black, background = magenta
    magentabg = '\033[1;30;45m'
    linha = '~' * 27
    print(f'{magentabg}{linha}\n  SISTEMA DE AJUDA PyHELP  \n{linha}')


def subtitle(resp):
    """
    Subtítulo do Sistema de Ajuda PyHELP.
    :param resp: Recebe o comando digitado pelo usuário para colocar no
    subtítulo.
    """
    # style = default, textcolor = black, background = cyan
    bluebg = '\033[30;46m'
    linha = '~' * (len(resp) + 36)
    print(f'{bluebg}{linha}'
          f'\n  Acessando o manual do comando \'{resp}\'  \n'
          f'{linha}')


def footer():
    """
    Mensagem de saída do Sistema de Ajuda PyHELP.
    """
    linha = '~' * 13
    # style = bold, textcolor = white, background = red
    redbg = '\033[1;97;41m'
    print(f'{redbg}{linha}\n  ATÉ LOGO!  \n{linha}')


# Main
class PyHelp:
    """
    Sistema que esclarece informações sobre o comando digitado pelo usuário.
    """
    # style = default, textcolor = black, background = white
    whitebg = '\033[30;107m'
    exitansi = '\033[m'
    while True:
        title()
        resp = str(input(f'{exitansi}Função ou Biblioteca > ')).strip()
        if resp.upper() == 'FIM':
            footer()
            break
        subtitle(resp.lower())
        print(f'{whitebg}')
        help(resp.lower())
