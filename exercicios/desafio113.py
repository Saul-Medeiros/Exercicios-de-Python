"""
Desafio 113 - Reescreva a função leiaInt() que fizemos no desafio 104,
incluíndo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""
cor = (
    '\033[31m',  # 0: Vermelho
    '\033[32m',  # 1: Verde
    '\033[33m',  # 2: Amarelo
    '\033[m'     # 3: Tira a cor
)


def msg():
    return f'\n{cor[2]}Usuário preferiu não digitar esse número.{cor[3]}'


def leiaint(prompt):
    while True:
        try:
            number = int(input(prompt))
        # caso valor informado não seja int
        except (ValueError, TypeError):
            print(f'{cor[0]}ERRO! Digite um número inteiro válido.{cor[3]}')
        # programa interrompido pelo usuário
        except KeyboardInterrupt:
            print(msg())
            number = 0
            break
        else:
            break
    return number


def leiafloat(prompt):
    while True:
        try:
            number = float(input(prompt))
        # caso valor informado não seja float
        except (ValueError, TypeError):
            print(f'{cor[0]}ERRO! Digite um número real válido.{cor[3]}')
        except KeyboardInterrupt:
            print(msg())
            return 0
        else:
            return number


n = leiaint('Digite um número inteiro: ')
f = leiafloat('Digite um número real: ')
print(f'{cor[1]}Você digitou o valor inteiro {n} e o valor real {f}.{cor[3]}')
