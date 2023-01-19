"""
Desafio 104 - Crie um programa que tenha a função leiaint(), que vai funcionar
de forma semelhante à função input() do Python, só que fazendo a validação para
aceitar apenas um valor numérico.
Ex:
n = leiaint('Digite um número:')
"""


def leiaint(prompt):
    """
    Função que verifica se a digitação é um número inteiro, caso contrário,
    vai repetir a chamada de dados até que seja informado um número válido.
    :param prompt: Informações de texto que serão mostradas no prompt.
    :return: Retorna o valor inteiro informado pelo usuário.
    """
    while True:
        # Variável local que receberá a entrada de dados do usuário.
        var = str(input(prompt)).strip()
        # Verifica se é um número inteiro
        if var.isnumeric():
            # Transforma de str para int
            var = int(var)
            break
        # Verifica se a variável está vazia ou se é texto
        else:
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
    return var


# Programa Principal
n = leiaint('Digite um número: ')
print(f'\033[32mVocê acabou de digitar o número {n}.\033[m')
