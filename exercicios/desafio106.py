"""
Desafio 106 - Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário
digitar a palavra 'FIM', o programa se encerrará.
OBS: use cores.
"""
cores = (
    '\033[1;30;45m',   # 0: background magenta
    '\033[30;46m',     # 1: background azul
    '\033[1;97;41m',   # 2: background vermelho
    '\033[30;107m',    # 3: background branco
    '\033[m'           # 4: tira cor
)


def textformat(msg, cor):
    """
    -> Formata a mensagem, centralizando ela entre duas linhas horizontais,
    que varia o tamanho de acordo com o tamanho do texto.
    :param msg: Mensagem a ser formatada
    :param cor: Cor a ser usada de fundo
    :return: Mensagem formatada com cores
    """
    linha = '~' * (len(msg) + 4)
    print(cor + linha)
    print(str(msg).center(len(msg) + 4))
    print(linha)


# Main
while True:
    textformat('SISTEMA DE AJUDA PyHELP', cores[0])
    resp = str(input(f'{cores[4]}Função ou Biblioteca > ')).strip()
    if resp.upper() == 'FIM':
        textformat('ATÉ LOGO!', cores[2])
        break
    textformat(f'Acessando o manual do comando\'{resp.lower()}\'', cores[1])
    print(cores[3])
    help(resp.lower())
